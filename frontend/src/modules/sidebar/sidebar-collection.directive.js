'use strict';

angular.module('squirrel').directive('sidebarCollection', function() {
  return {
    restrict: "E",
    replace: true,
    scope: {
      collection: '='
    },
    templateUrl: "modules/sidebar/sidebar-collection.template.html",
  }
})
