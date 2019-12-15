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
def _shell(script, serial):
    print os.popen('./shell/' + script + ' ' + serial).read().strip()
    return serial + ' ' + script


@app.route('/upload/<path>/<serial>', methods=['GET'])
def _upload(path, serial):
    return (
        '<!doctype html>'
        '<title>Upload File</title>'
        '<h1>Upload File</h1>'
        '<h3>Path: ' + path + '</h3>'
        '<h3>Serial: ' + serial + '</h3>'
        '<form method="post" enctype="multipart/form-data" action="/upload">'
        '<input type="file" name="file">'
        '<input type="submit" value="Upload">'
        '</form>'
    )


app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB
app.run(host='0.0.0.0', port=3001)
