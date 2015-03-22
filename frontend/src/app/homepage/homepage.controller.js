'use strict';

angular.module('squirrel').controller('HomepageCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS) {

      $scope.login_username = "";

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("homepage on loginSuccesful1:" + userName);
        $scope.login_username = userName;
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("homepage on logout");
        $scope.login_username = "";
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("homepage on loginError:" + error);
        $scope.login_username = "";
      });

    }
  ]
);
