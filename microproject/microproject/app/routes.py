from flask import Response, render_template, request
import requests
import hashlib
import redis
import psycopg2
from app import app


cache = redis.StrictRedis(host='redis', port=6379, db=0)


@app.route('/')
@app.route('/index')
def main():
    conn = psycopg2.connect(database="pgdb", user="pguser", password="pguser", host="dbpostgres", port="5432")

    return render_template('index.html', context=locals())


@app.route('/you-are')
def you_are():

    ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    user_agent = request.user_agent.string
    user_identification = ip_address + user_agent
    user_hash = hashlib.sha256(user_identification.encode()).hexdigest()

    return render_template('you_are.html', context=locals())


@app.route('/microproject-settings')
def microproject_settings():

    return render_template('microproject_settings.html', context=locals())


@app.route('/monster/<name>')
def get_identicon(name):

    image = cache.get(name)
    if image is None:
        print('Cache is miss')
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=160')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')