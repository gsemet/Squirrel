'use strict';

angular.module('squirrel').directive('portfolioSummary',

  [

    function() {
      return {
        replace: true,
        transclude: true,
        restrict: 'E',
        scope: {
          id: '@id',
        },
        controllerAs: "page",
        templateUrl: "modules/portfolio-summary/portfolio-summary.template.html",
        controller: "PortfolioSummaryDirectiveCtrl",
      };
    }
  ]
);
