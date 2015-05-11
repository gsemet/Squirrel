'use strict';

angular.module('squirrel').controller('FooterCtrl',

  ["$scope", "$location", "layout",

    function($scope, $location, layout) {
      $scope.show_footer = function() {
        return layout.showFooter();
      };
    }
  ]
);
