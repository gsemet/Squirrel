'use strict';

angular.module('squirrel').controller('PortfolioSummaryDirectiveCtrl',

  ["$scope", "gettextCatalog", "Restangular", "debug", "request",

    function($scope, gettextCatalog, Restangular, debug, request) {

      var basePortfolios = Restangular.all("api/portfolios/");
      $scope.portfolio = {};

      $scope.refresh = function() {
        basePortfolios.one("p", $scope.id).get().then(function(data) {
          debug.dump("PortfolioSummaryDirectiveCtrl", data, "portfolio details received");
          $scope.portfolio = data;
        });
      };

      $scope.refresh();
    }
  ]
);
