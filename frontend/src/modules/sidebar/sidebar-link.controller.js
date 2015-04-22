'use strict';

angular.module('squirrel').controller('SidebarLinkCtrl',

  ["$scope", "gettextCatalog", "$location",

    function($scope, gettextCatalog, $location) {
      $scope.currentPage = function(page) {
        var s = $location.search();
        if (_.isEmpty(s['p'])) {
          return "dashboard";
        }
        return s['p'];
      };

      $scope.activeIfCurrentPageIs = function(page) {
        var s = $location.search();
        var current_page = $scope.currentPage();
        /*console.log("activeIfCurrentPageIs");*/
        /*console.log("current_page = " + JSON.stringify(current_page));*/
        /*console.log("page = " + JSON.stringify(page));*/
        if (current_page == page) {
          return "active";
        }
        return "";
      };
    }
  ]
);
