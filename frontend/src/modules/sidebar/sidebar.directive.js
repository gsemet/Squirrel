'use strict';

angular.module('squirrel').directive('sidebar',

  [

    /**
     * Example:
     *
     *   http://sporto.github.io/blog/2013/06/24/nested-recursive-directives-in-angular/
     */

    function() {
      return {
        replace: true,
        transclude: false,
        restrict: 'E',
        scope: {
          "title": "@",
          "collection": "=",
        },
        templateUrl: "modules/sidebar/sidebar.template.html",
        controller: "SidebarCtrl",
      };
    }
  ]
);
