'use strict';

/**
 *
 * Inspired by
 *   https://github.com/coursera/js-libraries-snapshot/blob/master/js/lib/readme.js
 */

angular.module('squirrel').directive('banner',

  [

    function() {
      return {
        replace: true,
        transclude: true,
        restrict: 'E',
        scope: {
          bannerName: '@banner',
          bannerShowCount: "@bannerShowCount",
          bannerEnabled: "@bannerEnabled",
          bannerExpires: "@bannerExpires",
        },
        controllerAs: "page",
        templateUrl: "directives/banner/banner.template.html",
        controller: "BannerCtrl",
      };
    }
  ]
);
