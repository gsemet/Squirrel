'use strict';

angular.module("squirrel").controller("PortfolioOverviewCreateController",

  ["$scope", "$location", "gettextCatalog", "Restangular",

    function($scope, $location, gettextCatalog, Restangular) {

      $scope.portfolioTypes = {};
      $scope.currentType = null;

      $scope.refresh = function() {
        console.log("currentType = " + JSON.stringify($scope.currentType));
        if ($scope.currentType) {
          _.forEach($scope.types, function(item) {
            console.log("item = " + JSON.stringify(item));
            console.log("item.name = " + JSON.stringify(item.name));
            if (item.name == $scope.currentType) {
              $scope.portfolioTypes = {
                selected: item
              };
            }
          });
        }
      };

      $scope.getPortfolioTypes = function() {
        var basePortfolioTypes = Restangular.all("api/portfolios/types");

        basePortfolioTypes.getList().then(function(data) {
          console.log("received portfolios types: " + JSON.stringify(data));
          $scope.portfolioTypes = data;
          $scope.refresh();
        });
      };
      $scope.getPortfolioTypes();
    }
  ]
);
