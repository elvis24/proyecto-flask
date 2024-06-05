import redis
import time
from flask import Flask 

app =Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries==0:
                raise exc
            retries -=1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello world seen {} time.\n'.format(count)

@app.route('/about')
def about():
    return '<h1>Habla Papu</h1>'