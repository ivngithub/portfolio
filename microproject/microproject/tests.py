from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Feedback

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User(username='ivn', email='ivn@example.com')
        self.assertEqual(u.user_hash_for_avatar, 'ec21567262e72ab3a0a4b90c3f1e19ee84c2a35dcf92be70303cc5540036e202')

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_few_feedback(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        fb1 = Feedback(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        fb2 = Feedback(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        fb3 = Feedback(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
        fb4 = Feedback(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([fb1, fb2, fb3, fb4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u3)  # susan follows mary
        u3.follow(u4)  # mary follows david
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_few_feedback().all()
        f2 = u2.followed_few_feedback().all()
        f3 = u3.followed_few_feedback().all()
        f4 = u4.followed_few_feedback().all()
        self.assertEqual(f1, [fb2, fb4, fb1])
        self.assertEqual(f2, [fb2, fb3])
        self.assertEqual(f3, [fb3, fb4])
        self.assertEqual(f4, [fb4])

if __name__ == '__main__':
    unittest.main(verbosity=2)