'use strict';

angular.module('squirrel').controller('SidebarLinkCtrl',

  ["$scope", "gettextCatalog", "$location", "sidebar",

    function($scope, gettextCatalog, $location, sidebar) {

      $scope.activeIfCurrentPageIs = function(page) {
        var s = $location.search();
        if (sidebar.isInThisState(s, $scope.member)) {
          return "active";
        }
        return "";
      };

      $scope.getClass = function(page) {
        if ($scope.member.type == 'separator') {
          return "sidebar-separator";
        }
        return $scope.activeIfCurrentPageIs(page);
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
