'use strict';

angular.module("squirrel").controller("LoginCtrl",

  ["$scope", "$location", "AuthenticationService",

    function($scope, $location, AuthenticationService) {

      $scope.submit = function() {
        console.log("Sending login for user: " + JSON.stringify($scope.username));
        AuthenticationService.login($scope.username, $scope.password);
        $location.path("/");
      };

    }
  ]
);
