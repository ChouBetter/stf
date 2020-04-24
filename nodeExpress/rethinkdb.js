var express = require('express')
var r = require('rethinkdb')

var app = express()

const DB_HOST = 'localhost'

app.get('/allowDevices/:user', function (req, res) {
  console.log(`user: ${req.params.user}`)
  r.connect({
    host: DB_HOST,
    port: 28015
  }, function (err, conn, callback) {
    if (err)
      console.log(err)
    r.db("stf").table("users").filter({
      name: req.params.user
    }).limit(1).run(conn, (err, cursor) => {
      if (err)
        console.log(err)
      cursor.toArray(function (err, user) {
        if (err)
          console.log(err)
        console.log(user)
        var allowDevices = []
        if (user.length && user[0].hasOwnProperty("allowDevices")) {
          allowDevices = user[0].allowDevices
        }
        res.status(200).json({
          allowDevices: allowDevices
        })
      })
    });
  });
});

app.post('/allowDevices/update', express.json(), function (req, res) {
  var name = req.body.user;
  var allowDevices = req.body.allowDevices;
  console.log(`user: ${name}, allowDevices: ${allowDevices}`)
  r.connect({
    host: DB_HOST,
    port: 28015
  }, function (err, conn, callback) {
    if (err)
      console.log(err)
    r.db("stf").table("users").filter({
      name: name
    }).limit(1).run(conn, (err, cursor) => {
      cursor.toArray((err, user) => {
        if (user.length) {
          r.db("stf").table("users").filter({
            name: name
          }).update({
            allowDevices: allowDevices
          }).run(conn, (err, cursor) => {
            res.status(200).json({
              result: 0
            })
          });
        } else {
          r.db('stf').table("users").insert([{
            "createdAt": r.now(),
            "email": name + "@androidcloud.com",
            "forwards": [],
            "group": "FOPnIQ0mRJuwda/mi02kUg==",
            "ip": "::ffff:127.0.0.1",
            "lastLoggedInAt": r.now(),
            "name": name,
            "settings": {},
            "allowDevices": allowDevices
          }]).run(conn, (err, cursor) => {
            res.status(200).json({
              result: 0
            })
          });
        }
      })
    });
  });
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
