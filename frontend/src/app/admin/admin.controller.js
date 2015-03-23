'use strict';

// take ideas from:
// http://ironsummitmedia.github.io/startbootstrap-sb-admin/index.html
angular.module('squirrel').controller('AdminCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS) {

      $scope.is_admin = false;

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
