'use strict';

angular.module('squirrel').directive('sidebarSeparator', function($compile) {
  return {
    restrict: "E",
    replace: true,
    templateUrl: "modules/sidebar/sidebar-separator.template.html",
  }
})
