'use strict';

angular.module("squirrel").controller("MyPortfoliosCtrl",

  ["$scope", "AuthenticationService", "$rootScope", "AUTH_EVENTS",

    function($scope, AuthenticationService, $rootScope, AUTH_EVENTS) {

      $scope.is_logged = AuthenticationService.isAuthenticated();
      console.log("my portofolio is_logged = " + JSON.stringify($scope.is_logged));

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });
    }
  ]
);
