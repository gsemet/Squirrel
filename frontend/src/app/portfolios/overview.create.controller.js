'use strict';

angular.module("squirrel").controller("PortfolioOverviewCreateController",

  ["$scope", "$location", "gettextCatalog", "Restangular", "LocationWatcherService", "request",
  "$sce", "debug",

    function($scope, $location, gettextCatalog, Restangular, LocationWatcherService, request,
      $sce, debug) {

      $scope.portfolioTypes = {};
      $scope.currentType = null;
      $location.search("a", "create");

      $scope.refresh = function() {
        debug.dump("PortfolioOverviewCreateController", $scope.currentType, "$scope.currentType");
        if ($scope.currentType) {
          _.forEach($scope.types, function(item) {
            debug.dump("PortfolioOverviewCreateController", item, "item");
            debug.dump("PortfolioOverviewCreateController", item[0], "item[0]");
            debug.dump("PortfolioOverviewCreateController", item[1], "item[1]");
            if (item[1] == $scope.currentType) {
              $scope.portfolioTypes = {
                selected: item
              };
            }
          });
        }
      };

      $scope.getPortfolioTypes = function() {
        request.request("api/portfolios/types").then(function(data) {
          debug.dump("PortfolioOverviewCreateController", data, "received portfolios types");
          $scope.portfolioTypes = data;
          $scope.refresh();
          $scope.createPortfolio.$setPristine();
          $scope.createPortfolio.portfolioType.$setPristine();
        });
      };
      $scope.getPortfolioTypes();

      $scope.groupPerAccountTypes = function(item) {
        return item[0];
      };
      /*
      $scope.setupWatchers = function($scope, scopeVarName, nameKey) {
        $scope.$watch(function() {
          return $location.search();
        }, function() {
          $scope[scopeVarName] = $location.search()[nameKey] || "";
        });
        $scope.$watch(scopeVarName, function(portfolioName) {
          $location.search(nameKey, portfolioName);
        });
      };
      */
      LocationWatcherService.setupWatchers($scope, "portfolioName", "n");
      LocationWatcherService.setupWatchers($scope, "portfolioDescription", "d");
      LocationWatcherService.setupWatchers($scope, "portfolioTypes.selected[1]", "t");
    }
  ]
);
