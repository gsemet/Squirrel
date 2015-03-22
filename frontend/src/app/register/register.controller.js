'use strict';

angular.module("squirrel").controller("RegisterCtrl",

  ["$scope", "AuthenticationService", "$location",

    function($scope, AuthenticationService, $location) {

      $scope.registration_sent = false;
      $scope.registration_email = "";

      $scope.submit = function() {
        console.log("Sending login for user: " + JSON.stringify($scope.username));
        console.log("$scope.email = " + JSON.stringify($scope.email));
        $scope.registration_email = $scope.email;
        AuthenticationService.register($scope.username, $scope.email, $scope.password).then(function() {
          console.log("user registerd");
          $scope.registration_sent = true;
        });
      };
    }
  ]
);
