'use strict';

angular.module('squirrel').directive('sbSref',

  [

    /*
     * Inpired by
     *
     *   https://github.com/angular-ui/ui-router/blob/master/src/stateDirectives.js
     */

    function() {
      return {
        restrict: 'A',
        link: function(scope, element, attrs, uiSrefActive) {
          var ref = attrs.sbSref;
          var params = null;
          var url = null;
          // SVGAElement does not use the href attribute, but rather the 'xlinkHref' attribute.
          var hrefKind = Object.prototype.toString.call(element.prop('href')) === '[object SVGAnimatedString]' ?
            'xlink:href' : 'href';
          var newHref = null;
          var isAnchor = element.prop("tagName").toUpperCase() === "A";
          var isForm = element[0].nodeName === "FORM";
          var attr = isForm ? "action" : hrefKind;
          var nav = true;

          var update = function(newVal) {
            if (newVal) {
              params = angular.copy(newVal);
            }
            if (!nav) {
              return;
            }

            /*newHref = "new href value";*/
            /*attrs.$set(attr, newHref);*/
            attrs.$set("class", "sb-sref-cursor");
          };

          if (ref.paramExpr) {
            scope.$watch(ref.paramExpr, function(newVal, oldVal) {
              if (newVal !== params) {
                update(newVal);
              }
            }, true);
            params = angular.copy(scope.$eval(ref.paramExpr));
          }
          update();

          if (isForm) {
            return;
          }

          element.bind("click", function(e) {
            var button = e.which || e.button;
            if (!(button > 1 || e.ctrlKey || e.metaKey || e.shiftKey || element.attr('target'))) {

              console.log("click on sb-sref!!!");
            }
          });
        }
      }
    }
  ]
);
