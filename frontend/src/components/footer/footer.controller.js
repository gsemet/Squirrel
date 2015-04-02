'use strict';

angular.module('squirrel').controller('FooterCtrl',

  ["$scope", "$location",

    function($scope, $location) {
      $scope.show_footer = function() {
        if ($location.path() === "/" && page === '') {
          console.log("display footer on homepage!")
          return true;
        }
        var currentRoute = $location.path().substring(1) || '/';
        var hide_in_pages = [
          "/admin",
        ];
        var page = $location.path();
        /*console.log("page = " + JSON.stringify(page));*/
        var v = !_.contains(hide_in_pages, page);
        /*console.log("display footer: " + JSON.stringify(v));*/
        return v;
      };
    }
  ]
);
