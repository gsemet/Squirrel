'use strict';

/**
 * Usage:
 *
 * <magnific-popup>
 *  <div ng-repeat="image in images">
 *    <a href="{{image.src}}" class="image" title="{{image.title}}">
 *      <img src="{{image.src}}">
 *    </a>
 *  </div>
 *</div>
 *
 */
angular.module('squirrel').directive('magnific-popup',
  function() {

    return {
      restrict: 'A',
      link: function(scope, element, attrs) {

        var defaults = {};
        var options = angular.extend({}, defaults, scope.$eval(attrs.gallery));

        element.magnificPopup({
          delegate: options.selector,
          gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
          },
          image: {
            tError: 'Error: Unable to Load Image',
            titleSrc: function(item) {

              return item.el.attr('title');
            }
          },
          tLoading: 'Loading...',
          type: 'image'
        });
      }
    };
  }
);
