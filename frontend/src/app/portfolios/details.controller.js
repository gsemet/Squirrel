'use strict';

angular.module("squirrel").controller("PortfoliosDetailsCtrl",

  ["$scope", "$location", "$routeParams", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",

    function($scope, $location, $routeParams, gettextCatalog, Restangular, ngTableParams, $timeout) {

      var portfolio = {
        "id": $routeParams.portfolioId
      };

      $scope.refresh = function() {
        Restangular.one('api/portfolio', 123).ge().then(function(data) {
          $timeout(function() {
            console.log("received portfolio data for id " + portfolio.id + ": " + JSON.stringify(data));
            portfolio = data;
          }, 200);
        });
      };

      $timeout($scope.refresh, 50);
    }
  ]
);
