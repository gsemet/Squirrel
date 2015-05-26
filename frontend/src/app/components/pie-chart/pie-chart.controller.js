'use strict';

angular.module('squirrel').controller('PieChartCtrl',

  ["$scope", "gettextCatalog",

    function($scope, gettextCatalog) {

      $scope.config = {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
        },
        title: {
          text: $scope.title
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
          data: $scope.data,
        }]
      };

    }
  ]
);
