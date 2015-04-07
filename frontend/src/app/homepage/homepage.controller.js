'use strict';

angular.module('squirrel').controller('HomepageCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS) {

      $scope.logged_in = AuthenticationService.isAuthenticated();

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("homepage on loginSuccesful1:" + userName);
        $scope.logged_in = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("homepage on logout");
        $scope.logged_in = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("homepage on loginError:" + error);
        $scope.logged_in = false;
      });

    }
  ]
);
