'use strict';

angular.module('squirrel').controller('FooterCtrl',

  ["$scope",

    function($scope) {

      $show_footer = true;

      $scope.$show_footer = function(page) {
        /*console.log("location: " + $location.path() + ", page: " + page);*/
        if ($location.path() === "/" && page === '') {
          /*console.log("returning active!")*/
          return "active";
        }
        var currentRoute = $location.path().substring(1) || '/';
        return page === currentRoute ? 'active' : '';
      };
    }
  ]
);
