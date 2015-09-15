'use strict';

angular.module('squirrel').directive('pieChart',

  [

    function() {
      return {
        replace: true,
        transclude: true,
        restrict: 'E',
        scope: {
          title: "=title",
          data: '@data',
        },
        controllerAs: "page",
        templateUrl: "app/components/pie-chart/pie-chart.template.html",
        controller: "PieChartCtrl",
      };
    }
  ]
);
