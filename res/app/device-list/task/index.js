require("./device-list-task.css");

module.exports = angular
  .module("stf.device-list.task", [
    require("gettext").name,
    require("stf/user/group").name,
    require("stf/common-ui").name,
    require("../column").name,
    require("../empty").name,
    require("stf/standalone").name
  ])
  .directive("deviceListTask", require("./device-list-task-directive"));
