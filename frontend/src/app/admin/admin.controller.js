'use strict';

// take ideas from:
// http://startbootstrap.com/template-overviews/sb-admin/
// http://ironsummitmedia.github.io/startbootstrap-sb-admin/index.html
angular.module('squirrel').controller('AdminCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS", "ADMIN_PAGES", "$location", "_",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS, ADMIN_PAGES, $location, _) {

      $scope.is_admin = AuthenticationService.isAdmin();
      $scope.isPageDashboard = function() {
        var s = $location.search();
        console.log("admin page query = " + JSON.stringify(s));
        console.log("s.length = " + JSON.stringify(s.length));
        console.log("!s = " + JSON.stringify(!s));
        console.log("!!s = " + JSON.stringify(!!s));
        console.log("_.isEmpty(s) = " + JSON.stringify(_.isEmpty(s)));
        if (_.isEmpty(s)) {
          console.log("returning true");
          return true;
        }
        if (s['p'] === ADMIN_PAGES.dashboard) {
          return true;
        }
        return false;
      };

      $scope.isPageCharts = function() {
        var s = $location.search();
        console.log("admin page query = " + JSON.stringify(s));
        console.log("s['p'] == ADMIN_PAGES.charts = " + JSON.stringify(s['p'] == ADMIN_PAGES.charts));
        if (s['p'] == ADMIN_PAGES.charts) {
          return true;
        }
        return false;
      };

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("admin on loginSuccesful1:" + userName);
        $scope.is_admin = AuthenticationService.isAdmin();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("admin on logout");
        $scope.is_admin = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("admin on loginError:" + error);
        $scope.is_admin = false;
      });

    }
  ]
);
