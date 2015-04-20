'use strict';

angular.module("squirrel").controller("FeaturesCtrl",

  ["$scope", "$rootScope", "$location", "AuthenticationService", "$anchorScroll", "gettextCatalog",
  "$document",

    function($scope, $rootScope, $location, AuthenticationService, $anchorScroll, gettextCatalog,
      $document) {

      $scope.scrollTo = function(id) {
        /* $location.hash(id); */
        /* $anchorScroll(); */
        var offset = 130;
        var duration = 400; //milliseconds
        var targetElement = angular.element(document.getElementById(id));
        // use duScroll for smooth scrolling
        $document.scrollToElement(targetElement, offset, duration);
      };

      $rootScope.$on('$duScrollChanged', function($event, scrollY) {
        console.log('Scrolled to ', scrollY);
      });

      $scope.items = [
        {
          "key": "center-history",
          "text": gettextCatalog.getString("Center of your Finance")
        }, {
          "key": "visualizations",
          "text": gettextCatalog.getString("Visual Reporting")
        }, {
          "key": "anywhere",
          "text": gettextCatalog.getString("Anywhere, Anytime")
        }, {
          "key": "share",
          "text": gettextCatalog.getString("Share your Portfolio")
        }, {
          "key": "faq",
          "text": gettextCatalog.getString("FAQ")
        }
      ];
    }
  ]
);
