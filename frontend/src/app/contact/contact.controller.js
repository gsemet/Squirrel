'use strict';

angular.module("squirrel").controller("ContactCtrl",

  ["$scope", "$location", "AuthenticationService",

    function($scope, $location, AuthenticationService) {

      $scope.message_sent = false;
      $scope.submit = function() {
        console.log("Sending message for user: " + JSON.stringify($scope.email));
        $scope.message_sent = true;
      };

    }
  ]
);
