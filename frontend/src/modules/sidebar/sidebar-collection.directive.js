'use strict';

angular.module('squirrel').directive('sidebarCollection', function() {
  return {
    restrict: "E",
    replace: true,
    scope: {
      collection: '=',
      expand: '@'
    },
    templateUrl: "modules/sidebar/sidebar-collection.template.html",
    controller: "SidebarCollectionCtrl",
  }
})
