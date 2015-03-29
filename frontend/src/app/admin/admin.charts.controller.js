'use strict';

angular.module('squirrel').controller('AdminChartsCtrl',

  ['$scope', '$http',

    function($scope, $http) {

      $scope.chartConfig = {
        options: {
          chart: {
            zoomType: 'x'
          },
          rangeSelector: {
            enabled: true
          },
          navigator: {
            enabled: true
          }
        },
        series: [],
        title: {
          text: 'Sample of stock'
        },
        useHighStocks: true
      }

      $scope.chartConfig.series.push({
          id: 1,
          data: [
                  [1147651200000, 23.15],
                  [1147737600000, 23.01],
                  [1147824000000, 22.73],
                  [1147910400000, 22.83],
                  [1147996800000, 22.56],
                  [1148256000000, 22.88],
                  [1148342400000, 22.79],
                  [1148428800000, 23.50],
                  [1148515200000, 23.74],
                  [1148601600000, 23.72],
                  [1148947200000, 23.15],
                  [1149033600000, 22.65]
              ]
        }, {
          id: 2,
          data: [
                  [1147651200000, 25.15],
                  [1147737600000, 25.01],
                  [1147824000000, 25.73],
                  [1147910400000, 25.83],
                  [1147996800000, 25.56],
                  [1148256000000, 25.88],
                  [1148342400000, 25.79],
                  [1148428800000, 25.50],
                  [1148515200000, 26.74],
                  [1148601600000, 26.72],
                  [1148947200000, 26.15],
                  [1149033600000, 26.65]
              ]
        }

      );

      $scope.chartConfig2 = {
        options: {
          chart: {
            type: 'bar'
          }
        },
        series: [{
          data: [10, 15, 12, 8, 7]
          }],
        title: {
          text: 'sample of bar'
        },

        loading: false
      };

      //////////////////////////////////////////////////////////////////////////////////////////////

      $scope.chartConfig3 = {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false
        },
        title: {
          text: 'Browser market shares'
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
        series: [
          {
            type: 'pie',
            name: 'Browser share',
            data: [
                    ['Firefox', 45.0],
                    ['IE', 26.8],
              {
                name: 'Chrome',
                y: 12.8,
                sliced: true,
                selected: true
                    },
                    ['Safari', 8.5],
                    ['Opera', 6.2],
                    ['Others', 0.7]
                ]
            }
        ]
      };

      //////////////////////////////////////////////////////////////////////////////////////////////

      $http.get("../app/admin/eurusd.json").then(
        function(result) {
          console.log("request sent:" + +JSON.stringify(result.data));

          $scope.chartEurUsdConfig = {

            title: {
              text: 'AAPL stock price by minute'
            },

            subtitle: {
              text: 'Using explicit breaks for nights and weekends'
            },

            xAxis: {
              breaks: [{ // Nights
                from: Date.UTC(2011, 9, 6, 16),
                to: Date.UTC(2011, 9, 7, 8),
                repeat: 24 * 36e5
              }, { // Weekends
                from: Date.UTC(2011, 9, 7, 16),
                to: Date.UTC(2011, 9, 10, 8),
                repeat: 7 * 24 * 36e5
              }]
            },

            rangeSelector: {
              buttons: [{
                type: 'hour',
                count: 1,
                text: '1h'
              }, {
                type: 'day',
                count: 1,
                text: '1D'
              }, {
                type: 'all',
                count: 1,
                text: 'All'
              }],
              selected: 1,
              inputEnabled: false
            },

            series: [{
              name: 'AAPL',
              type: 'area',
              data: result.data,
              gapSize: 5,
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
              }]
          }
        });
      //////////////////////////////////////////////////////////////////////////////////////////////
    }
  ]
);
