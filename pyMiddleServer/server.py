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

@app.route('/auto/<serial>/<script>')
def setting(serial, script):
	# print os.popen('docker exec -it appium1 adb connect ' + serial).read().strip()
	# print '---------------------------------------------------------------'
	print os.popen('python script/' + script + ' ' + serial).read().strip()
	# print '---------------------------------------------------------------'
	# print os.popen('docker exec -it appium1 adb disconnect ' + serial).read().strip()
	return serial + ' ' + script

app.run(host='0.0.0.0',port=3001)
