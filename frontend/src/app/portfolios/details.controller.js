'use strict';

angular.module("squirrel").controller("PortfoliosDetailsCtrl",

  ["$scope", "$location", "$routeParams", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",

    function($scope, $location, $routeParams, gettextCatalog, Restangular, ngTableParams, $timeout) {
      $scope.portfolio = {};
      $scope.displayed = [];

      $scope.refresh = function() {
        var s = $location.search();
        var wanted_id = s['i'];
        Restangular.one('api/portfolios/p', wanted_id).get().then(function(data) {
          $timeout(function() {
            console.log("received portfolio data for id " + wanted_id + ": " + JSON.stringify(data));
            $scope.portfolio = data;
            console.log("$scope.portfolio.name = " + JSON.stringify($scope.portfolio.name));
            $scope.refreshGraphs();
            $scope.refreshTable();
          }, 50);
        });
      };

      $timeout($scope.refresh, 50);

      $scope.chartConfigAllocation = {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
        },
        title: {
          text: gettextCatalog.getString("Securities Allocation")
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: false
            },
            showInLegend: false
          }
        },
        series: [{
          type: 'pie',
          name: 'Share',
          data: [],
        }]
      };

      $scope.chartConfigHistory = {
        options: {
          chart: {
            //zoomType: 'x'
          },
          rangeSelector: {
            enabled: true,
            buttons: [{
              type: 'month',
              count: 1,
              /// 2 letters to say "1 month"
              text: gettextCatalog.getString('1m'),
              }, {
              type: 'month',
              count: 3,
              /// 2 letters to say "3 months"
              text: gettextCatalog.getString('3m'),
              }, {
              type: 'month',
              count: 6,
              /// 2 letters to say "6 months"
              text: gettextCatalog.getString('6m'),
              }, {
              type: 'ytd',
              /// 3 letters to say "year-to-date"
              text: gettextCatalog.getString('YTD'),
              }, {
              type: 'year',
              count: 1,
              /// 2 letters to say "1 year"
              text: gettextCatalog.getString('1y'),
              }, {
              type: 'all',
              /// 3 letters to say "all"
              text: gettextCatalog.getString('All'),
              }],
          },
          scollbar: {
            enabled: false,
          },
          navigator: {
            enabled: true
          }
        },
        series: [],
        title: {
          text: gettextCatalog.getString('Valorisation history')
        },
        useHighStocks: true
      };

      $scope.refreshGraphs = function() {
        $scope.refreshGraphHistory();
        $scope.refreshGraphAllocation();
      };

      $scope.refreshGraphAllocation = function() {
        var data = [];
        _.forEach($scope.portfolio.details, function(stock) {
          data.push({
            name: stock.name,
            y: +stock.valorisation.v,
          });
        });
        $scope.chartConfigAllocation.series[0].data = data;
        console.log("replacing chartConfigAllocation.series = " + JSON.stringify(data));
      };


      $scope.refreshGraphHistory = function() {
        var data = [];
        _.forEach($scope.portfolio.valorisation_history.history, function(h) {
          data.push([+h.e, +h.v]);
        });

        $scope.chartConfigHistory.series.push({
          id: 1,
          data: data,
          name: $scope.portfolio.name,
          type: 'area',
          gapSize: 0,
          tooltip: {
            valueDecimals: 2
          },
          fillColor: {
            linearGradient: {
              x1: 0,
              y1: 0,
              x2: 0,
              y2: 1
            },
            stops: [
                [0, Highcharts.getOptions().colors[0]],
                [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
          },
          threshold: null
        });
        console.log("replacing chartConfigHistory.series = " + JSON.stringify(data));
      };

      $scope.refreshTable = function() {
        $scope.displayed = $scope.portfolio.details;
      }
    }
  ]
);
