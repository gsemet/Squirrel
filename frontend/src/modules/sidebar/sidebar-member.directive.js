'use strict';

angular.module('squirrel').directive('sidebarMember', function($compile) {
  return {
    restrict: "E",
    replace: true,
    scope: {
      member: '=',
    },
    controller: 'SidebarMemberCtrl',
    link: function(scope, element, attrs) {
      console.log("scope.member = " + JSON.stringify(scope.member));
      if (scope.member.type == "separator") {
        element.append("<sidebar-separator></sidebar-separator>");
        $compile(element.contents())(scope)
      } else {
        element.append("<sidebar-link member='member'></sidebar-separator>");
        $compile(element.contents())(scope)
      }
    }
  }
})
