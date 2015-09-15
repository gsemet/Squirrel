'use strict';

angular.module("squirrel").controller("PortfoliosSummaryCtrl",

  ["$scope", "$location", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",
  "ModalService", "debug", "PortfolioCreateService", "request",

    function($scope, $location, gettextCatalog, Restangular, ngTableParams, $timeout,
      ModalService, debug, PortfolioCreateService, request) {

      var s = $location.search();
      $scope.portfolio_id = s["i"];
      debug.dump("PortfoliosSummaryCtrl", $scope.portfolio_id, "$scope.portfolio_id");
      if ($scope.portfolio_id) {
        debug.info("PortfoliosSummaryCtrl", "We are in portfolio detail, leaving overview controller initialization");
        return;
      }

      var basePortfolios = Restangular.all("api/portfolios/p");

      $scope.portfolios = [];
      $scope.refresh = function() {
        $scope.portfolios = [];
        basePortfolios.getList().then(function(data) {
          debug.dump("PortfoliosSummaryCtrl", data, "received portfolios data");
          _.forEach(data, function(row) {
            $scope.portfolios.push(row);
          });
        });

        request.request("api/portfolios/a").then(function(data) {
          debug.dump("PortfoliosSummaryCtrl", data, "summary of all portfolios received");
          $scope.all_portfolio = data;
        });
      };

      $timeout($scope.refresh, 200);

      $scope.edit = function(row) {
        debug.log("PortfoliosSummaryCtrl", "edit row = " + JSON.stringify(row));
        $location.search("i", row.id);
        $scope.portfolio_id = row.id;
      };

      $scope.createPortfolio = function() {
        PortfolioCreateService.createPortfolio();
      };

      var action = s["a"];
      if (action == "create") {
        debug.log("PortfoliosSummaryCtrl", "a=create, creating portfolios!!");
        $timeout($scope.createPortfolio, 100);
      }
    }
  ]
);

angular.module('squirrel').filter('portfolio_summary_detail_popover', function() {

  return function(row) {
    var output;
    output = "Description: " + row.description + "\n";
    output += "Name: " + row.name + "\n";
    return output;
  }
});
