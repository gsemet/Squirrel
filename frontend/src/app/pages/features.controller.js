'use strict';

angular.module("squirrel").controller("FeaturesCtrl",

  ["$scope", "$location", "AuthenticationService", "$anchorScroll",

    function($scope, $location, AuthenticationService, $anchorScroll) {

      $scope.scrollTo = function(id) {
        $location.hash(id);
        $anchorScroll();
      };

    }
  ]
);
