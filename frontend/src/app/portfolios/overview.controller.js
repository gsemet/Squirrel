'use strict';

angular.module("squirrel").controller("PortfoliosOverviewCtrl",

  ["$scope", "$location", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",

    function($scope, $location, gettextCatalog, Restangular, ngTableParams, $timeout) {

      var basePortfolios = Restangular.all("api/portfolios");

      $scope.displayed = [];
      $scope.refresh = function() {
        $scope.displayed = [];
        basePortfolios.getList().then(function(data) {
          $timeout(function() {
            console.log("received portfolios data: " + JSON.stringify(data));
            _.forEach(data, function(row) {
              $scope.displayed.push(row);
            });
          }, 300);
        });
      };

      $timeout($scope.refresh, 200);
    }
  ]
);
