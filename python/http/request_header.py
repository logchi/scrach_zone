# coding=utf-8
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    origin = request.headers.get('origin', '*')
    print(origin)
    return 'the http header field origin is {}'.format(origin)

@app.route('/env/')
def env():
    print(os.environ)
    return 'the environment of the operating system is {}'.format(os.environ)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="9876")