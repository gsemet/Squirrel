'use strict';

angular.module('squirrel').controller('SidebarCtrl',

  ["$scope", "gettextCatalog",

    function($scope, gettextCatalog) {
      $scope.expand = false;
    }
  ]
);
