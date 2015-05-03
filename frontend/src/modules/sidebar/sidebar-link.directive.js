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
      /*if (angular.isArray(scope.member.children)) {
          element.append(
            "<sidebar-collection collection='member.children' expand='false'></sidebar-collection>"
          );
          $compile(element.contents())(scope)
        }
      }*/
      var collectionSt = '<sidebar-collection collection="member.children" expand="false"></sidebar-collection>';
      if (angular.isArray(scope.member.children)) {
        $compile(collectionSt)(scope, function(cloned, scope) {
          element.append(cloned);
        });
      }
    }
  }
})
