require("./device-list-usings.css");

module.exports = angular
  .module("stf.device-list.usings", [
    require("gettext").name,
    require("stf/user/group").name,
    require("stf/common-ui").name,
    require("../column").name,
    require("../empty").name,
    require("stf/standalone").name
  ])
  .directive("deviceListUsings", require("./device-list-usings-directive"));
