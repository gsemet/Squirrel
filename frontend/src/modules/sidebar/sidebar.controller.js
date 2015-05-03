'use strict';

angular.module('squirrel').controller('SidebarCtrl',

  ["$scope", "gettextCatalog", "sidebar", "$location", "debug", "$timeout",

    function($scope, gettextCatalog, sidebar, $location, debug, $timeout) {

      $scope.templateUrl = undefined;

      $scope.toggleSidebar = function() {
        sidebar.toggleOpened();
        $scope.refreshClass();
        debug.debug("SidebarCtrl", "sidebar toggle => " + $scope.sidebar_class);
      };

      $scope.includeCurrentPage = function() {
        debug.debug("SidebarCtrl", "includeCurrentPage !!!");
      };

      $scope.refreshClass = function() {
        $scope.sidebar_class = sidebar.isOpened() ? "active" : "";
        if (sidebar.isFirstTime()) {
          debug.debug("SidebarCtrl", "is first time the page is displayed! animate sidebar !");
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
        debug.debug("SidebarCtrl", "NAVIGATE event received");
        debug.debug("SidebarCtrl", "order show content of " + JSON.stringify($scope.templateUrl));
        debug.debug("SidebarCtrl", "update search to " + JSON.stringify(member.search));
        $location.search(member.search);
      });

      $scope.$on(sidebar.DISPLAY_PAGE, function(event, member) {
        $scope.templateUrl = member.templateUrl;
        debug.debug("SidebarCtrl", "DISPLAY_PAGE page event received");
        debug.debug("SidebarCtrl", "order show content of " + JSON.stringify($scope.templateUrl));
      });

      $scope.$on(sidebar.REFRESH_SIDEBAR, function(event) {
        debug.debug("SidebarCtrl", "Sidebar controller received order to refresh itself");
        debug.dump("SidebarCtrl", $scope.collection, "$scope.collection");
        $timeout(function() {
          debug.log("SidebarCtrl", "refreshing sidebar");
          $scope.$digest();
        }, 500);
      });

      $scope.refreshFromCurrentLocation = function(collection) {
        var search = $location.search();
        /*debug.debug("SidebarCtrl", "refresh from location = " + JSON.stringify(search));*/
        _.forEach($scope.collection, function(itemCollection) {
          if (sidebar.isInThisState(search, itemCollection)) {
            /*debug.info("sidebar", "I found we actually are on page: " +
              JSON.stringify(itemCollection) + ". Displaying it");*/
            $scope.$emit(sidebar.DISPLAY_PAGE, itemCollection);
          }
        });
      };
      $scope.refreshFromCurrentLocation($scope.collection);
    }
  ]
);
