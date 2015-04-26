'use strict';

angular.module("squirrel").controller("RegisterCtrl",

  ["$scope", "AuthenticationService", "$location", "$document",

    function($scope, AuthenticationService, $location, $document) {

      $document.scrollTo(0, 0);
      $scope.registration_sent = false;
      $scope.registration_email = "";

      $scope.submit = function() {
        console.log("Sending login for first name: " + JSON.stringify($scope.first_name));
        console.log("Sending login for last name: " + JSON.stringify($scope.last_name));
        console.log("$scope.email = " + JSON.stringify($scope.email));
        $scope.registration_email = $scope.email;
        AuthenticationService.register($scope.first_name, $scope.last_name, $scope.email, $scope.password).then(
          function() {
            console.log("user registerd");
            $scope.registration_sent = true;
          });
      };
    }
  ]
);
