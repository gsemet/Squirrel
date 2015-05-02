'use strict';

angular.module('squirrel').controller('SidebarCtrl',

  ["$scope", "gettextCatalog", "sidebar", "$location", "debug",

    function($scope, gettextCatalog, sidebar, $location, debug) {

      $scope.templateUrl = undefined;

      $scope.toggleSidebar = function() {
        sidebar.toggleOpened();
        $scope.refreshClass();
        debug.log("sidebar", "sidebar toggle => " + $scope.sidebar_class);
      };

      $scope.includeCurrentPage = function() {
        debug.log("sidebar", "includeCurrentPage !!!");
      };

      $scope.refreshClass = function() {
        $scope.sidebar_class = sidebar.isOpened() ? "active" : "";
        if (sidebar.isFirstTime()) {
          debug.debug("sidebar", "is first time the page is displayed! animate sidebar !");
          $scope.sidebar_class += " sidebar-nav-animate";
          $scope.sidebar_transition = "sidebar-transition";
          return
        }
        $scope.sidebar_transition = "";
      };

      debug.info("sidebar", "Creating sidebar controller");
      $scope.refreshClass();

      $scope.$on(sidebar.NAVIGATE, function(event, member) {
        $scope.templateUrl = member.templateUrl;
        debug.log("sidebar", "update search to " + JSON.stringify(member.search));
        debug.log("sidebar", "order show content of " + JSON.stringify($scope.templateUrl));
        $location.search(member.search);
      });

      $scope.refreshFromCurrentLocation = function(collection) {
        var search = $location.search();
        debug.debug("sidebar", "refresh from location = " + JSON.stringify(search));
        _.forEach($scope.collection, function(itemCollection) {
          if (sidebar.isInThisState(search, itemCollection)) {
            debug.info("sidebar", "I found we actually are on page: " +
              JSON.stringify(itemCollection) + "Navigating to it");
            $scope.$emit(sidebar.NAVIGATE, itemCollection);
          }
        });
      };
      $scope.refreshFromCurrentLocation($scope.collection);
    }
  ]
);
