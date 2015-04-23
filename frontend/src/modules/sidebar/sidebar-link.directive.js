'use strict';

angular.module('squirrel').directive('sidebarLink', function($compile) {
  return {
    restrict: "E",
    replace: true,
    scope: {
      member: '=',
    },
    controller: 'SidebarLinkCtrl',
    templateUrl: "modules/sidebar/sidebar-link.template.html",
    link: function(scope, element, attrs) {
      if (angular.isArray(scope.member.children)) {
        element.append("<sidebar-collection collection='member.children'></sidebar-collection>");
        $compile(element.contents())(scope)
      }
    }
  }
})
