'use strict';

angular.module("squirrel").controller("PortfoliosSummaryCtrl",

  ["$scope", "$location", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",
  "ModalService", "debug", "PortfolioCreateService",

    function($scope, $location, gettextCatalog, Restangular, ngTableParams, $timeout,
      ModalService, debug, PortfolioCreateService) {

      /*var basePortfolios = Restangular.all("api/portfolios/p");

      $scope.displayed = [];
      $scope.refresh = function() {
        $scope.displayed = [];
        basePortfolios.getList().then(function(data) {
          $timeout(function() {
            debug.log("PortfoliosSummaryCtrl", "received portfolios data: " + JSON.stringify(data));
            _.forEach(data, function(row) {
              $scope.displayed.push(row);
            });
          }, 300);
        });
      };

      $timeout($scope.refresh, 200);*/

      var s = $location.search();
      $scope.portfolio_id = s["i"];
      debug.dump("PortfoliosSummaryCtrl", $scope.portfolio_id, "$scope.portfolio_id");
      if ($scope.portfolio_id) {
        debug.info("PortfoliosSummaryCtrl", "We are in portfolio detail, leaving overview controller initialization");
        return;
      }

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
