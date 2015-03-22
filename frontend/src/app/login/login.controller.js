angular.module("squirrel").controller("LoginCtrl",

  ["$scope", "AuthenticationService",

    function($scope, AuthenticationService) {

      $scope.submit = function() {
        console.log("Sending login for user: " + JSON.stringify($scope.username));
        AuthenticationService.login($scope.username, $scope.password);
      };

    }
  ]
);
