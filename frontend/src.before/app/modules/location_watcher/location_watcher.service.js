'use strict';


angular.module('squirrel').factory('LocationWatcherService',

  ["$location",

    function($location) {

      var service = {}

      service.setupWatchers = function($scope, scopeVarName, nameKey) {
        $scope.$watch(function() {
          return $location.search();
        }, function() {
          $scope[scopeVarName] = $location.search()[nameKey] || "";
        });

        $scope.$watch(scopeVarName, function(portfolioName) {
          $location.search(nameKey, portfolioName);
        });
      };

      return service;
    }
  ]
);
