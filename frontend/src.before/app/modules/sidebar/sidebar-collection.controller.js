'use strict';

angular.module('squirrel').controller('SidebarCollectionCtrl',

  ["$scope", "gettextCatalog", "$location", "sidebar", "debug",

    function($scope, gettextCatalog, $location, sidebar, debug) {

      debug.log("SidebarCollectionCtrl", "$scope.expand = " + JSON.stringify($scope.expand));

      $scope.$on(sidebar.TOGGLE_GROUP, function(event, member) {
        $scope.expand = !$scope.expand;
        debug.log("SidebarCollectionCtrl", "toogle group to " + $scope.expand);
      });

    }
  ]
);
