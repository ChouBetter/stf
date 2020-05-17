var QueryParser = require("./util/query-parser");

module.exports = function DeviceListCtrl(
  $scope,
  DeviceService,
  DeviceColumnService,
  GroupService,
  ControlService,
  SettingsService,
  $location
) {
  $scope.tracker = DeviceService.trackAll($scope);
  $scope.control = ControlService.create($scope.tracker.devices, "*ALL");

  $scope.columnDefinitions = DeviceColumnService;

  var defaultColumns = [{
      name: "state",
      selected: true
    },
    {
      name: "model",
      selected: true
    },
    {
      name: "name",
      selected: true
    },
    {
      name: "serial",
      selected: false
    },
    {
      name: "operator",
      selected: true
    },
    {
      name: "releasedAt",
      selected: true
    },
    {
      name: "version",
      selected: true
    },
    {
      name: "network",
      selected: false
    },
    {
      name: "display",
      selected: false
    },
    {
      name: "manufacturer",
      selected: false
    },
    {
      name: "sdk",
      selected: false
    },
    {
      name: "abi",
      selected: false
    },
    {
      name: "cpuPlatform",
      selected: false
    },
    {
      name: "openGLESVersion",
      selected: false
    },
    {
      name: "browser",
      selected: false
    },
    {
      name: "phone",
      selected: false
    },
    {
      name: "imei",
      selected: false
    },
    {
      name: "imsi",
      selected: false
    },
    {
      name: "iccid",
      selected: false
    },
    {
      name: "batteryHealth",
      selected: false
    },
    {
      name: "batterySource",
      selected: false
    },
    {
      name: "batteryStatus",
      selected: false
    },
    {
      name: "batteryLevel",
      selected: false
    },
    {
      name: "batteryTemp",
      selected: false
    },
    {
      name: "provider",
      selected: true
    },
    {
      name: "notes",
      selected: true
    },
    {
      name: "owner",
      selected: true
    }
  ];

  $scope.columns = defaultColumns;

  $scope.scripts = [{
    name: "script1",
    script: "script1.py"
  }, {
    name: "script2",
    script: "script2.py"
  }, {
    name: "script3",
    script: "script3.py"
  }];

  $scope.triggerScript = function () {
    var script = document.getElementById("script").value;
    alert(script);
    console.log($scope.tracker.devices);
    for (var idx in $scope.tracker.devices) {
      var device = $scope.tracker.devices[idx]
      console.log(device);
      if (device.using)
        fetch(`http://${document.location.hostname}:3001/auto/${device.serial}/${script}`)
        .then(function (response) {
          return response;
        })
        .catch(function (err) {});
    }
  };

  SettingsService.bind($scope, {
    target: "columns",
    source: "deviceListColumns"
  });

  var defaultSort = {
    fixed: [{
      name: "state",
      order: "asc"
    }],
    user: [{
      name: "name",
      order: "asc"
    }]
  };

  $scope.sort = defaultSort;

  SettingsService.bind($scope, {
    target: "sort",
    source: "deviceListSort"
  });

  $scope.filter = [];

  $scope.activeTabs = {
    icons: true,
    details: false,
    usings: false,
    task: false,
    mgr: false,
    aloc: false,
    upload: false,
    mgr2: false
  };

  SettingsService.bind($scope, {
    target: "activeTabs",
    source: "deviceListActiveTabs"
  });

  $scope.toggle = function (device) {
    if (device.using) {
      $scope.kick(device);
    } else {
      $location.path("/control/" + device.serial);
    }
  };

  $scope.invite = function (device) {
    return GroupService.invite(device).then(function () {
      $scope.$digest();
    });
  };

  $scope.applyFilter = function (query) {
    $scope.filter = QueryParser.parse(query);
  };

  $scope.search = {
    deviceFilter: "",
    focusElement: false
  };

  $scope.focusSearch = function () {
    if (!$scope.basicMode) {
      $scope.search.focusElement = true;
    }
  };

  $scope.reset = function () {
    $scope.search.deviceFilter = "";
    $scope.filter = [];
    $scope.sort = defaultSort;
    $scope.columns = defaultColumns;
  };
};
