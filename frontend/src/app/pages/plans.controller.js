'use strict';

angular.module("squirrel").controller("PlansCtrl",

  ["$scope", "$location", "AuthenticationService", "$document", "gettextCatalog",

    function($scope, $location, AuthenticationService, $document, gettextCatalog) {

      $document.scrollTo(0, 0);

      /* Adapt odd_class and even_class to have nice display on the screen! */

      $scope.features = [
        {
          "name": gettextCatalog.getString("Portfolio Control"),
          "odd_class": "light",
          "even_class": "",
          "features": [
            {
              "description": gettextCatalog.getString('View and Edit all your Portfolios'),
              "free": true,
              "premium": true,
            },
            {
              "description": gettextCatalog.getString("Weekly / Daily Portfolio Report by email"),
              "free": true,
              "premium": true,
            },
            {
              "description": gettextCatalog.getString("Quaterly Portfolio Report by email"),
              "free": true,
              "premium": true,
            }
          ]
        },
        {
          "name": gettextCatalog.getString("Measure"),
          "odd_class": "",
          "even_class": "light",
          "features": [
            {
              "description": gettextCatalog.getString("Return, Gain, Alpha"),
              "free": true,
              "premium": true,
            },
            {
              "description": gettextCatalog.getString("Share price"),
              "free": true,
              "premium": true,
            }
          ]
        }
      ]
    }
  ]
);
