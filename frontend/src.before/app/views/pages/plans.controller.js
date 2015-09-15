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
              "description": gettextCatalog.getString('View and Edit one Portfolio'),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString('Number of Portfolios'),
              "free": 2,
              "premium": "unlimited",
            }, {
              "description": gettextCatalog.getString('Group Your Portfolios into Classes'),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString('Track Every Assets Type'),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString('Automatic Stocks, Mutual Funds, ETF Updates'),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("All Exchange Places"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Weekly / Daily Portfolio Report by email"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Personal History Timeline"),
              "free": true,
              "premium": true,
            }
          ]
        }, {
          "name": gettextCatalog.getString("Data Visualisation"),
          "odd_class": "light",
          "even_class": "",
          "features": [
            {
              "description": gettextCatalog.getString("Return, Gain, Alpha"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Tax-aware Return"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Share Price History"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Geography Exposure"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Small/Big Caps Exposure"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Assets Classes Exposure"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Compare With N Benchmarks (Stocks, Funds, ETF)"),
              "free": true,
              "premium": true,
            }
          ]
        }, {
          "name": gettextCatalog.getString("Stocks Screener"),
          "odd_class": "light",
          "even_class": "",
          "features": [
            {
              "description": gettextCatalog.getString("Dynamic Stocks Comparison"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Smart Stock Search History"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Save Screener Settings"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Screener Staging Area"),
              "free": true,
              "premium": true,
            }
          ]
        }, {
          "name": gettextCatalog.getString("Reports and Reminder"),
          "odd_class": "light",
          "even_class": "",
          "features": [
            {
              "description": gettextCatalog.getString("User defined Periodic Reminder for Manual Updates"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Weekly / Daily Portfolio Report by email"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Quaterly Portfolio Report by email"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Annual Portfolio Report edition"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Edit your annual Portfolio Report"),
              "free": true,
              "premium": true,
            }
          ]
        }, {
          "name": gettextCatalog.getString("Tax Statement"),
          "odd_class": "light",
          "even_class": "",
          "features": [
            {
              "description": gettextCatalog.getString("Easy Gains/Loose Tracking for your Tax Statement"),
              "free": true,
              "premium": true,
            }, {
              "description": gettextCatalog.getString("Speculative Account Monthly Report Storage"),
              "free": true,
              "premium": true,
            },
          ]
        }
      ]
    }
  ]
);
