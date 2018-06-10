from flask import Flask, Response, render_template, request
import requests
import hashlib
import redis


app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = 'Unique_salt'
default_name = 'ivn'


@app.route('/')
def main():

    return render_template('index.html')


@app.route('/you-are')
def you_are():

    ip_address = request.remote_addr
    user_agent = request.user_agent
    req = dir(request)
    hdrs = dir(request.headers)
    hdrs_dict = request.headers.__dict__
    headers = request.headers
    ip = request.headers.get('X-Real-IP')
    list_ip = request.headers.getlist('X-Forwarded-For')

    return render_template('you_are.html', context=locals())


@app.route('/temp', methods=['GET', 'POST'])
def mainpage():

    name = default_name
    if request.method == 'POST':
        name = request.form['name']
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title></title></head><body>'
    body = '''<form method="POST">
        Hello <input type="text" name="name" value="{}">
        <input type="submit" value="submit">
        </form>
        <p>You look like a:
        <img src="/monster/{}"/>               
    '''.format(name, name_hash)
    footer ='</body></html>'

    return header + body + footer


@app.route('/monster/<name>')
def get_identicon(name):

    image = cache.get(name)
    if image is None:
        print('Cache is miss')
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=160')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8001)
    app.run(debug=True, host='0.0.0.0', port=5000)
