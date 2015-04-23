'use strict';

angular.module('squirrel').controller('SidebarCtrl',

  ["$scope", "gettextCatalog", "sidebar", "$location",

    function($scope, gettextCatalog, sidebar, $location) {

      $scope.templateUrl = undefined;

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

      $scope.$on(sidebar.NAVIGATE, function(event, member) {
        $scope.templateUrl = member.templateUrl;
        console.log("update search to " + JSON.stringify(member.search));
        console.log("order show content of " + JSON.stringify($scope.templateUrl));
        $location.search(member.search);
      });

      $scope.refreshFromLocation = function(collection) {
        var search = $location.search();
        console.log("refresh from location = " + JSON.stringify(search));
        _.forEach($scope.collection, function(itemCollection) {
          console.log("item search = " + JSON.stringify(itemCollection.search));
          var allFound = false;
          _.forEach(search, function(itemSearch, itemSearchkey) {
            console.log("itemSearch = " + JSON.stringify(itemSearchkey) + " " +
              JSON.stringify(itemSearch));
            if (itemCollection[itemSearchkey] == itemSearch) {
              allFound = true;
            }
          });
          if (allFound) {
            console.log("found we are on page = " + JSON.stringify(itemCollection));
            $scope.$emit(sidebar.NAVIGATE, itemCollection);
          }
        });
      };
      $scope.refreshFromLocation($scope.collection);
    }
  ]
);
