'use strict';

angular.module('squirrel').directive('sidebar',

  [

    function() {
      return {
        replace: true,
        transclude: true,
        restrict: 'E',
        scope: {},
        controllerAs: "page",
        templateUrl: "modules/sidebar/sidebar.template.html",
        controller: "SidebarCtrl",
      };
    }
  ]
);
