# coding=utf-8
from flask import Flask, redirect, request, jsonify
# from flask_cors import CORS, cross_origin
import requests
import os
import base64
import ldap
import ldap.modlist as modlist

LDAP_SERVER = "ldap://localhost:389/"
LDAP_BIND = "cn=admin,dc=androidcloud,dc=cn"
LDAP_BIND_PASS = "^andr0id2019$"
LDAP_BASE_DN = "dc=androidcloud,dc=cn"

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

    account = account.encode('utf-8')
    password = password.encode('utf-8')

    add_cn = account.split("@")[0]
    add_dc = account.split("@")[1].split(".")

    dn = ''
    if owner == '':
        dn = "cn=" + add_cn + ",dc=" + add_dc[0] + ",dc=" + add_dc[1]
    else:
        owner = owner.encode('utf-8')
        own_cn = owner.split("@")[0]
        own_dc = owner.split("@")[1]
        if own_dc == account.split("@")[1]:
            dn = "cn=" + add_cn + ",cn=" + own_cn + \
                ",dc=" + add_dc[0] + ",dc=" + add_dc[1]
        else:
            dn = "cn=" + add_cn + ",dc=" + add_dc[0] + ",dc=" + add_dc[1]

    attrs = {}
    attrs['objectclass'] = ['inetOrgPerson']
    attrs['cn'] = add_cn
    attrs['mail'] = account
    attrs["givenName"] = add_cn
    attrs["sn"] = add_cn
    attrs["userPassword"] = password
    attrs['description'] = 'ini group untuk semua dosen dokter'
    if owner != '':
        attrs['o'] = owner.encode('utf-8')

    print(dn)

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

    return jsonify(result)


@app.route('/sub/<account>')
def _sub(account):
    l = ldap.initialize(LDAP_SERVER)
    print("ldap.initialize")
    print(l.simple_bind_s(LDAP_BIND, LDAP_BIND_PASS))
    print("l.simple_bind_s")

    try:
        result = l.search_s(LDAP_BASE_DN, ldap.SCOPE_SUBTREE,
                            "o="+account.encode('utf-8'), None)
        print("l.search_s")
    except Exception as e:
        l.unbind_s()
        print("l.unbind_s")
        return str(e)

    l.unbind_s()
    print("l.unbind_s")

    return jsonify(result)


@app.route('/search/<account>')
def _search(account):
    l = ldap.initialize(LDAP_SERVER)
    print("ldap.initialize")
    print(l.simple_bind_s(LDAP_BIND, LDAP_BIND_PASS))
    print("l.simple_bind_s")

    account = account.encode('utf-8')
    acc_cn = account.split("@")[0]
    # ac_dc = account.split("@")[1].split(".")
    # dn = "cn=" + acc_cn + ",dc=" + ac_dc[0] + ",dc=" + ac_dc[1]

    try:
        result = l.search_s(
            LDAP_BASE_DN, ldap.SCOPE_SUBTREE, "cn=" + acc_cn, None)
        print("l.search_s")
    except Exception as e:
        l.unbind_s()
        print("l.unbind_s")
        return str(e)

    l.unbind_s()
    print("l.unbind_s")

    return jsonify(result)


app.run(host='0.0.0.0', port=3002)
