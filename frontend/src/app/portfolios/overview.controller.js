'use strict';

angular.module("squirrel").controller("PortfoliosOverviewCtrl",

  ["$scope", "$location", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",

    function($scope, $location, gettextCatalog, Restangular, ngTableParams) {

      var basePortfolios = Restangular.all("api/portfolios");

      // sample:
      //   http://plnkr.co/edit/zuzcma?p=info
      //
      $scope.tablePortfolios = new ngTableParams({
        page: 1, // show first page
        count: 20, // count per page
        sorting: {
          name: 'asc' // initial sorting
        }
      }, {
        total: 0, // length of data
        getData: function($defer, params) {
          console.log("params.url() = " + JSON.stringify(params.url()));
          basePortfolios.getList().then(function(portfolios) {
            $timeout(function() {
              console.log("portfolios = " + JSON.stringify(portfolios));
              // update table params
              params.total(portfolios.total);
              // set new data
              $defer.resolve(portfolios.result);
            }, 500);
          });
        },
      });
    }
  ]
);
