'use strict';

angular.module('squirrel').controller('BannerCtrl',

  ["$scope", "gettextCatalog", "ipCookie", "amMoment",

    function($scope, gettextCatalog, ipCookie, amMoment) {

      // inspirated by:
      //   https://github.com/coursera/js-libraries-snapshot/blob/master/js/lib/readme.js

      $scope.staticEnabled = true;

      $scope.visible = function() {
        if (!$scope.isEnabled()) {
          return false;
        }
        if (!$scope.bannerShowCount) {
          return true;
        }
        var count = $scope.getCount();
        ipCookie($scope.getCookieName(), count);
        var bannerShowCount = parseInt($scope.bannerShowCount, 10);
        if (count < bannerShowCount) {
          return true;
        }
        return false;
      };

      $scope.closeBanner = function() {
        if (!$scope.bannerShowCount) {
          $scope.staticEnabled = false;
          $scope.visible();
          return;
        }
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

      $scope.isEnabled = function() {
        if ($scope.bannerEnabled && $scope.bannerEnabled == "true") {
          return $scope.staticEnabled;
        } else {
          return false;
        }
      };
    }
  ]
);
