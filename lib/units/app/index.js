var http = require("http");
var url = require("url");
var fs = require("fs");

var express = require("express");
var validator = require("express-validator");
var cookieSession = require("cookie-session");
var bodyParser = require("body-parser");
var serveFavicon = require("serve-favicon");
var serveStatic = require("serve-static");
var csrf = require("csurf");
var compression = require("compression");
const request = require("request");

var r = require("rethinkdb");

var logger = require("../../util/logger");
var pathutil = require("../../util/pathutil");

var auth = require("./middleware/auth");
var deviceIconMiddleware = require("./middleware/device-icons");
var browserIconMiddleware = require("./middleware/browser-icons");
var appstoreIconMiddleware = require("./middleware/appstore-icons");

var markdownServe = require("markdown-serve");

const USER_MAIL_PATTERN = "@androidcloud.cn";
const RDB_HOST = "localhost";
const PY_LDAP_HOST = "localhost";

module.exports = function (options) {
  var log = logger.createLogger("app");
  var app = express();
  var server = http.createServer(app);

  app.use(
    "/static/wiki",
    markdownServe.middleware({
      rootDirectory: pathutil.root("node_modules/stf-wiki"),
      view: "docs",
    })
  );

  app.set("view engine", "pug");
  app.set("views", pathutil.resource("app/views"));
  app.set("strict routing", true);
  app.set("case sensitive routing", true);
  app.set("trust proxy", true);

  if (fs.existsSync(pathutil.resource("build"))) {
    log.info("Using pre-built resources");
    app.use(compression());
    app.use(
      "/static/app/build/entry",
      serveStatic(pathutil.resource("build/entry"))
    );
    app.use(
      "/static/app/build",
      serveStatic(pathutil.resource("build"), {
        maxAge: "10d",
      })
    );
  } else {
    log.info("Using webpack");
    // Keep webpack-related requires here, as our prebuilt package won't
    // have them at all.
    var webpackServerConfig = require("./../../../webpack.config")
      .webpackServer;
    app.use(
      "/static/app/build",
      require("./middleware/webpack")(webpackServerConfig)
    );
  }

  app.use(
    "/static/bower_components",
    serveStatic(pathutil.resource("bower_components"))
  );
  app.use("/static/app/data", serveStatic(pathutil.resource("data")));
  app.use(
    "/static/app/status",
    serveStatic(pathutil.resource("common/status"))
  );
  app.use("/static/app/browsers", browserIconMiddleware());
  app.use("/static/app/appstores", appstoreIconMiddleware());
  app.use("/static/app/devices", deviceIconMiddleware());
  app.use("/static/app", serveStatic(pathutil.resource("app")));

  app.use("/static/logo", serveStatic(pathutil.resource("common/logo")));
  app.use(serveFavicon(pathutil.resource("common/logo/exports/STF-128.png")));

  app.use("/html", serveStatic(pathutil.resource("common/html")));

  app.use(
    cookieSession({
      name: options.ssid,
      keys: [options.secret],
    })
  );

  app.use(
    auth({
      secret: options.secret,
      authUrl: options.authUrl,
    })
  );

  // This needs to be before the csrf() middleware or we'll get nasty
  // errors in the logs. The dummy endpoint is a hack used to enable
  // autocomplete on some text fields.
  app.all("/app/api/v1/dummy", function (req, res) {
    res.send("OK");
  });

  app.post("/app/api/v1/allowDevices/update", express.json(), function (
    req,
    res
  ) {
    var name = req.body.user;
    var allowDevices = req.body.allowDevices;
    console.log(`user: ${name}, allowDevices: ${allowDevices}`);
    r.connect({
        host: RDB_HOST,
        port: 28015,
      },
      function (err, conn, callback) {
        if (err) console.log(err);
        r.db("stf")
          .table("users")
          .get(name).update({
            allowDevices: allowDevices
          })
      }
    );
  });

  app.use(bodyParser.json());
  app.use(csrf());
  app.use(validator());

  app.use(function (req, res, next) {
    res.cookie("XSRF-TOKEN", req.csrfToken());
    next();
  });

  app.get("/", function (req, res) {
    res.render("index");
  });

  app.get("/app/api/v1/pyLDAP", function (req, res) {
    console.log(req.user.name);
    var reqURl = `http://${PY_LDAP_HOST}:3002${req.query.param}/${req.user.email}`;
    console.log("URL:", reqURl);
    request(reqURl, function (error, response, body) {
      console.error("error:", error); // Print the error if one occurred
      console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
      console.log("body:", body); // Print the HTML for the Google homepage.
      if (error) res.status(200).send(error);
      else if (!response) res.status(200).send("No response");
      else res.status(response.statusCode).send(body);
    });
  });

  app.get("/app/api/v1/pyLDAP/add/:account/:password/:allow", function (req, res) {
    console.log(req.user.name);
    var reqURl = `http://${PY_LDAP_HOST}:3002/add/${req.params.account}/${req.params.password}/${req.user.email}`;
    console.log("URL:", reqURl);
    request(reqURl, function (error, response, body) {
      console.error("error:", error); // Print the error if one occurred
      console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
      console.log("body:", body); // Print the HTML for the Google homepage.
      if (error) res.status(200).send(error);
      else if (!response) res.status(200).send("No response");
      else {
        r.connect({
            host: RDB_HOST,
            port: 28015,
          },
          function (err, conn, callback) {
            if (err) console.log(err);
            r.db("stf")
              .table("users")
              .insert([{
                createdAt: r.now(),
                email: req.params.account,
                forwards: [],
                group: "FOPnIQ0mRJuwda/mi02kUg==",
                ip: "::ffff:127.0.0.1",
                lastLoggedInAt: r.now(),
                name: req.params.account.split("@")[0],
                settings: {},
                allowDevices: [],
                allowAdd: req.params.allow == "true" ? 1 : 0
              }, ])
              .run(conn, (err, cursor) => {
                res.status(response.statusCode).send(body);
              });
          }
        );
      }
    });
  });

  app.get("/app/api/v1/pyMiddle", function (req, res) {
    var reqURl = `http://${req.query.host}:3001${req.query.param}`;
    console.log("URL:", reqURl);
    request(reqURl, function (error, response, body) {
      console.error("error:", error); // Print the error if one occurred
      console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
      console.log("body:", body); // Print the HTML for the Google homepage.
      if (error) res.status(200).send(error);
      else if (!response) res.status(200).send("No response");
      else res.status(response.statusCode).send(body);
    });
  });

  app.get("/app/api/v1/allowDevices/:user", function (req, res) {
    console.log(`user: ${req.params.user}`);
    r.connect({
        host: RDB_HOST,
        port: 28015,
      },
      function (err, conn, callback) {
        if (err) console.log(err);
        r.table("users").get(req.params.user).run(conn, function (err, result) {
          console.log(result)
          var allowDevices = [];
          if (result.allowDevices) {
            allowDevices = result.allowDevices;
          }
          res.status(200).json({
            allowDevices: allowDevices,
          });
        });

      }
    );
  });

  app.get("/app/api/v1/sensors", function (req, res) {
    var reqURl = `http://${req.query.host}:18000/sensors`;
    console.log("URL:", reqURl);
    request(reqURl, function (error, response, body) {
      console.error("error:", error); // Print the error if one occurred
      console.log("statusCode:", response && response.statusCode); // Print the response status code if a response was received
      console.log("body:", body); // Print the HTML for the Google homepage.
      if (error) res.status(200).send(error);
      else if (!response) res.status(200).send("No response");
      else res.status(response.statusCode).send(body);
    });
  });

  app.get("/app/api/v1/logout", function (req, res) {
    //req.session.destroy();
    //req.session.cookie.expires = new Date().getTime();
    req.session = null;
    /*
    cookie = req.cookies;
    for (var prop in cookie) {
      if (!cookie.hasOwnProperty(prop)) {
        continue;
      }
      res.cookie(prop, '', {
        expires: new Date(0)
      });
    }
    */
    res.redirect("/");
  });

  app.get("/app/api/v1/state.js", function (req, res) {
    var state = {
      config: {
        websocketUrl: (function () {
          var wsUrl = url.parse(options.websocketUrl, true);
          wsUrl.query.uip = req.ip;
          return url.format(wsUrl);
        })(),
      },
      user: req.user,
    };

    if (options.userProfileUrl) {
      state.config.userProfileUrl = (function () {
        return options.userProfileUrl;
      })();
    }

    res.type("application/javascript");
    res.send("var GLOBAL_APPSTATE = " + JSON.stringify(state));
  });

  server.listen(options.port);
  log.info("Listening on port %d", options.port);
};
