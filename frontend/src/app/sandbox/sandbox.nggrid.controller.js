'use strict';

angular.module('squirrel').controller('SandboxNgGridCtrl',

  ['$scope', "Restangular", "ngTableParams", '$timeout',

    function($scope, Restangular, ngTableParams, $timeout) {

      //////////////////////////////////////////////////////////////////////////////////////////////
      $scope.myData = [{
          name: "Moroni",
          age: 50
        },
        {
          name: "Tiancum",
          age: 43
        },
        {
          name: "Jacob",
          age: 27
        },
        {
          name: "Nephi",
          age: 29
        },
        {
          name: "Enos",
          age: 34
        }];
      $scope.gridOptions = {
        data: 'myData',
        enableCellSelection: true
      };

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
          basePortfolios.getList().then(function(data) {
            $timeout(function() {
              console.log("received portfolios data: " + JSON.stringify(data));
              $defer.resolve(data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }, 500);
          });
        },
      });
    }
  ]
);
