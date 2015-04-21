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
          "text": gettextCatalog.getString("Center of your Finance"),
          "children": [
            {
              "key": "visualizations",
              "text": gettextCatalog.getString("Visual Portfolios")
            }, {
              "key": "anywhere",
              "text": gettextCatalog.getString("Anywhere, Anytime")
            }, {
              "key": "share",
              "text": gettextCatalog.getString("Share your Portfolio")
            }
          ]
        }, {
          "key": "what",
          "text": gettextCatalog.getString("Meet Squirrel"),
          "children": [
            {
              "key": "what",
              "text": gettextCatalog.getString("What is Squirrel?")
            }, {
              "key": "who",
              "text": gettextCatalog.getString("Who is it for?")
            }
          ]
        }, {
          "key": "faq",
          "text": gettextCatalog.getString("FAQ"),
          "children": []
        }
      ];

      $scope.chartConfig = {
        title: {
          text: 'Combination chart'
        },
        xAxis: {
          categories: ['Apples', 'Oranges', 'Pears', 'Bananas', 'Plums']
        },
        labels: {
          items: [{
            html: 'Total fruit consumption',
            style: {
              left: '50px',
              top: '18px',
              color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
            }
            }]
        },
        series: [{
          type: 'column',
          name: 'Jane',
          data: [3, 2, 1, 3, 4]
        }, {
          type: 'column',
          name: 'John',
          data: [2, 3, 5, 7, 6]
        }, {
          type: 'column',
          name: 'Joe',
          data: [4, 3, 3, 9, 0]
        }, {
          type: 'spline',
          name: 'Average',
          data: [3, 2.67, 3, 6.33, 3.33],
          marker: {
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[3],
            fillColor: 'white'
          }
        }, {
          type: 'pie',
          name: 'Total consumption',
          data: [{
            name: 'Jane',
            y: 13,
            color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
            name: 'John',
            y: 23,
            color: Highcharts.getOptions().colors[1] // John's color
            }, {
            name: 'Joe',
            y: 19,
            color: Highcharts.getOptions().colors[2] // Joe's color
            }],
          center: [100, 80],
          size: 100,
          showInLegend: false,
          dataLabels: {
            enabled: false
          }
        }]
      };
    }
  ]
);
