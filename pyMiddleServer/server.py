# coding=utf-8
from flask import Flask, redirect, request
import requests
import json
import commentjson
import os


def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        return 'You can close this window and terminate the script.'
    else:
        func()
        return 'Server is shutting down, so you can close this window.'


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return "success"


@app.route('/auto/<script>/<serial>')
def _auto(script, serial):
    print os.popen('python script/' + script + ' ' + serial).read().strip()
    return serial + ' ' + script


@app.route('/shell/<script>/<serial>')
def _auto(script, serial):
    print os.popen('./shell/' + script + ' ' + serial).read().strip()
    return serial + ' ' + script


app.run(host='0.0.0.0', port=3001)
