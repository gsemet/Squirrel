'use strict';

// take ideas from:
// http://startbootstrap.com/template-overviews/sb-admin/
// http://ironsummitmedia.github.io/startbootstrap-sb-admin/index.html
angular.module('squirrel').controller('SandboxCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS", "$location",
  "gettextCatalog",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS, $location,
      gettextCatalog) {

      $scope.is_admin = AuthenticationService.isAdmin();
      $scope.endpoint = "#/sandbox";

      $scope.menuItems = [
        {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
        }, {
          'type': 'separator',
        }, {
          'search': {
            "p": "charts"
          },
          'name': gettextCatalog.getString('Ex: Charts'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': "has children",
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html',
          'children': [{
              'search': {
                "p": "nggrid"
              },
              'name': gettextCatalog.getString('Ex: NgGrid'),
              'icon': 'fa fa-book',
              'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
            },
            {
              'type': 'separator',
            }, {
              'search': {},
              'name': gettextCatalog.getString('Dashboard'),
              'icon': 'glyphicon glyphicon-dashboard',
              'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
            }
          ]
        }, {
          'search': {
            "p": "charts"
          },
          'name': gettextCatalog.getString('Ex: Charts'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': gettextCatalog.getString('Ex: NgGrid'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
        }, {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
        }, {
          'search': {
            "p": "charts"
          },
          'name': gettextCatalog.getString('Ex: Charts'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': gettextCatalog.getString('Ex: NgGrid'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
        }, {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
        }, {
          'search': {
            "p": "charts"
          },
          'name': gettextCatalog.getString('Ex: Charts'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': gettextCatalog.getString('Ex: NgGrid'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
        }, {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
        }, {
          'search': {
            "p": "charts"
          },
          'name': gettextCatalog.getString('Ex: Charts'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': gettextCatalog.getString('Ex: NgGrid'),
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
        }, {
          'search': {},
          'name': gettextCatalog.getString('Dashboard'),
          'icon': 'glyphicon glyphicon-dashboard',
          'templateUrl': 'app/sandbox/sandbox.dashboard.template.html'
        }, {
          'search': {
            "p": "charts"
          },
          'name': 'avant dernier element',
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.charts.template.html'
        }, {
          'search': {
            "p": "nggrid"
          },
          'name': 'last item',
          'icon': 'fa fa-book',
          'templateUrl': 'app/sandbox/sandbox.nggrid.template.html'
        }
      ];
      $scope.currentPage = function(page) {
        var s = $location.search();
        if (_.isEmpty(s['p'])) {
          return "dashboard";
        }
        return s['p'];
      };

      $scope.activeIfCurrentPageIs = function(page) {
        var s = $location.search();
        var current_page;
        if (_.isEmpty(s['p'])) {
          current_page = "dashboard";
        } else {
          current_page = s['p'];
        }
        console.log("activeIfCurrentPageIs");
        console.log("current_page = " + JSON.stringify(current_page));
        console.log("page = " + JSON.stringify(page));
        if (current_page == page) {
          return "active";
        }
        return "";
      };

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("sandbox on loginSuccesful1:" + userName);
        $scope.is_admin = AuthenticationService.isAdmin();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("sandbox on logout");
        $scope.is_admin = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("sandbox on loginError:" + error);
        $scope.is_admin = false;
      });

    }
  ]
);
