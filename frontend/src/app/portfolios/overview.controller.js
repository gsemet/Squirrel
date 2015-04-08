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

      $scope.edit = function(row) {
        console.log("edit row = " + JSON.stringify(row));
        $location.url("/api/portfolio/details/" + row.id)
      };
    }
  ]
);

angular.module('squirrel').filter('portfolio_overview_detail_popover', function() {

  return function(row) {
    var output;
    output = "Description: " + row.description + "\n";
    output += "Name: " + row.name + "\n";
    return output;
  }
});
