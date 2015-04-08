'use strict';

angular.module("squirrel").controller("PortfoliosDetailsCtrl",

  ["$scope", "$location", "$routeParams", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",

    function($scope, $location, $routeParams, gettextCatalog, Restangular, ngTableParams, $timeout) {
      $scope.portfolio = {};
      $scope.refresh = function() {
        var s = $location.search();
        var wanted_id = s['i'];
        Restangular.one('api/portfolios', wanted_id).get().then(function(data) {
          $timeout(function() {
            console.log("received portfolio data for id " + wanted_id + ": " + JSON.stringify(data));
            $scope.portfolio = data;
            console.log("$scope.portfolio.name = " + JSON.stringify($scope.portfolio.name));
            $scope.refreshGraphs();
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
            showInLegend: true
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
            enabled: false
          },
          navigator: {
            enabled: false
          }
        },
        series: [],
        title: {
          text: gettextCatalog.getString('Valorisation history')
        },
        useHighStocks: true,
      }

      $scope.refreshGraphs = function() {
        var data = [];
        _.forEach($scope.portfolio.details, function(stock) {
          data.push({
            name: stock.name,
            y: +stock.valorisation.value,
          });
        });

        $scope.chartConfigAllocation.series[0].data = data;
        console.log("replacing chartConfigAllocation.series = " + JSON.stringify(data));

        data = [];
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
    }
  ]
);
