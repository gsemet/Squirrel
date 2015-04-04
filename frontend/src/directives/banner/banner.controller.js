'use strict';

angular.module('squirrel').controller('BannerCtrl',

  ["$scope", "gettextCatalog", "ipCookie", "amMoment",

    function($scope, gettextCatalog, ipCookie, amMoment) {

      // inspirated by:
      //   https://github.com/coursera/js-libraries-snapshot/blob/master/js/lib/readme.js

      $scope.visible = function() {
        var count = $scope.getCount();
        ipCookie($scope.getCookieName(), count);
        var bannerShowCount = parseInt($scope.bannerShowCount, 10);
        if (count < bannerShowCount) {
          return true;
        }
        return false;
      };

      $scope.closeBanner = function() {
        var count = $scope.getCount();
        ++count;
        ipCookie($scope.getCookieName(), count);
        $scope.visible();
      };

      $scope.getCookieName = function() {
        return "banner-" + $scope.bannerName;
      };

      $scope.getCount = function() {
        var times;

        var cookieContent = ipCookie($scope.getCookieName());
        if (!cookieContent) {
          return 0;
        }
        return parseInt(cookieContent, 10);
      };
    }
  ]
);
