var express = require("express");
var r = require("rethinkdb");

var app = express();

const DB_HOST = "123.51.133.103";

app.get("/allowDevices/:user", function (req, res) {
  console.log(`user: ${req.params.user}`);
  r.connect(
    {
      host: DB_HOST,
      port: 28015,
    },
    function (err, conn, callback) {
      if (err) console.log(err);
      r.db("stf")
        .table("users")
        .get(req.params.user)
        .run(conn, (err, result) => {
          if (err) console.log(err);
          console.log(result);
          res.status(200).json({
            allowDevices:
              result && result.hasOwnProperty("allowDevices")
                ? result.allowDevices
                : [],
          });
        });
    }
  );
});

app.post("/allowDevices/update", express.json(), function (req, res) {
  var name = req.body.user;
  var allowDevices = req.body.allowDevices;
  console.log(`user: ${name}, allowDevices: ${allowDevices}`);
  r.connect(
    {
      host: DB_HOST,
      port: 28015,
    },
    function (err, conn, callback) {
      if (err) console.log(err);
      r.db("stf")
        .table("users")
        .filter({
          name: name,
        })
        .limit(1)
        .run(conn, (err, cursor) => {
          cursor.toArray((err, user) => {
            if (user.length) {
              r.db("stf")
                .table("users")
                .filter({
                  name: name,
                })
                .update({
                  allowDevices: allowDevices,
                })
                .run(conn, (err, cursor) => {
                  res.status(200).json({
                    result: 0,
                  });
                });
            } else {
              r.db("stf")
                .table("users")
                .insert([
                  {
                    createdAt: r.now(),
                    email: name + "@androidcloud.com",
                    forwards: [],
                    group: "FOPnIQ0mRJuwda/mi02kUg==",
                    ip: "::ffff:127.0.0.1",
                    lastLoggedInAt: r.now(),
                    name: name,
                    settings: {},
                    allowDevices: allowDevices,
                  },
                ])
                .run(conn, (err, cursor) => {
                  res.status(200).json({
                    result: 0,
                  });
                });
            }
          });
        });
    }
  );
});

app.listen(3000, function () {
  console.log("Example app listening on port 3000!");
});
