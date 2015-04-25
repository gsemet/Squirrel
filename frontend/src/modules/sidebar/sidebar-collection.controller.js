'use strict';

angular.module('squirrel').controller('SidebarCollectionCtrl',

  ["$scope", "gettextCatalog", "$location", "sidebar",

    function($scope, gettextCatalog, $location, sidebar) {

      console.log("$scope.expand = " + JSON.stringify($scope.expand));

      $scope.$on(sidebar.TOGGLE_GROUP, function(event, member) {
        $scope.expand = !$scope.expand;
        console.log("toogle group to " + $scope.expand);
      });

    }
  ]
);
