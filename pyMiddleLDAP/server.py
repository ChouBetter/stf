# coding=utf-8
from flask import Flask, redirect, request
# from flask_cors import CORS, cross_origin
import requests
import json
import commentjson
import os
import base64
import ldap
import ldap.modlist as modlist

LDAP_SERVER = "ldap://localhost:389/"
LDAP_BIND = "cn=admin,dc=androidcloud,dc=cn"
LDAP_BIND_PASS = "^andr0id2019$"
LDAP_ADD_DN = ",dc=androidcloud,dc=cn"

app = Flask(__name__, static_url_path='/static')
# CORS(app)


@app.route('/')
def index():
    return "success"


@app.route('/add/<account>/<password>')
def _add(account, password):
    return _add_o(account, password, '')


@app.route('/add/<account>/<password>/<owner>')
def _add_o(account, password, owner):
    l = ldap.initialize(LDAP_SERVER)
    print("ldap.initialize")
    print(l.simple_bind_s(LDAP_BIND, LDAP_BIND_PASS))
    print("l.simple_bind_s")

    dn = ''
    if owner == '':
        dn = "cn=" + account + LDAP_ADD_DN
    else:
        dn = "cn=" + account + ",cn=" + owner + LDAP_ADD_DN

    account = account.encode('utf-8')
    password = password.encode('utf-8')

    attrs = {}
    attrs['objectclass'] = ['inetOrgPerson']
    attrs['cn'] = account
    attrs['mail'] = account + "@androidcloud.cn"
    attrs["givenName"] = account
    attrs["sn"] = account
    attrs["userPassword"] = password
    attrs['description'] = 'ini group untuk semua dosen dokter'

    ldif = modlist.addModlist(attrs)
    print("modlist.addModlist")

    try:
        result = l.add_s(dn, ldif)
        print("l.add_s")
    except Exception as e:
        l.unbind_s()
        print("l.unbind_s")
        return str(e)

    l.unbind_s()
    print("l.unbind_s")

    return str(result)


app.run(host='0.0.0.0', port=3002)
