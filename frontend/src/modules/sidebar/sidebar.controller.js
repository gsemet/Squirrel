'use strict';

angular.module('squirrel').controller('SidebarCtrl',

  ["$scope", "gettextCatalog", "sidebar",

    function($scope, gettextCatalog, sidebar) {

      $scope.toggleSidebar = function() {
        sidebar.toggleOpened();
        $scope.refreshClass();
        console.log("sidebar toggle => " + $scope.sidebar_class);
      };

      $scope.includeCurrentPage = function() {
        console.log("includeCurrentPage !!!");
      };

      $scope.refreshClass = function() {
        $scope.sidebar_class = sidebar.isOpened() ? "active" : "";
        if (sidebar.isFirstTime()) {
          console.log("is first time ! animate!");
          $scope.sidebar_class += " sidebar-nav-animate";
          $scope.sidebar_transition = "sidebar-transition";
          return
        }
        $scope.sidebar_transition = "";
      };


      console.log("Creating sidebar controller");
      $scope.refreshClass();
    }
  ]
);
