'use strict';

angular.module('squirrel').controller('PorfolioSummaryCtrl',

  ["$scope", "gettextCatalog", "Restangular", "debug",

    function($scope, gettextCatalog, Restangular, debug) {
      var basePortfolios = Restangular.all("api/portfolios/");

      $scope.displayed = [];
      $scope.refresh = function() {
        $scope.displayed = [];
        basePortfolios.one("p", $scope.id).get().then(function(data) {
          debug.dump("PorfolioSummaryCtrl", data, "reponse from server");
          $scope.data = data;
        });
      };

      $scope.refresh();
    }
  ]
);
