'use strict';

angular.module('squirrel').controller('SidebarLinkCtrl',

  ["$scope", "gettextCatalog", "$location", "sidebar",

    function($scope, gettextCatalog, $location, sidebar) {

      $scope.active = function(page) {
        var s = $location.search();
        if (sidebar.isInThisState(s, $scope.member)) {
          return true;
        }
        return false;
      };

      $scope.separator = function(page) {
        if ($scope.member.type == 'separator') {
          return true;
        }
        return false
      };

      $scope.onClick = function(member) {
        console.log("click on link = " + JSON.stringify(member));
        $scope.$emit(sidebar.NAVIGATE, member);
      };
      $scope.onChevronClick = function(member) {
        console.log("click on chevron = " + JSON.stringify(member));
        $scope.expand = !$scope.expand;
        $scope.$broadcast(sidebar.TOGGLE_GROUP, member);
      };

      $scope.hasChildren = function() {
        return angular.isArray($scope.member.children);
      };
    }
  ]
);
