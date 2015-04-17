'use strict';

var app;

// we use lodash is better than undercore: http: //kitcambridge.be/blog/say-hello-to-lo-dash/
app = angular.module("squirrel", [
  // keep the following lines sorted!
  'angular-parallax',
  'angular-timeline',
  'angularModalService',
  'angularMoment',
  'duScroll',
  'gettext',
  'highcharts-ng',
  'ipCookie',
  'mgcrea.ngStrap',
  'ngAnimate',
  'ngCrossfilter',
  'ngGrid',
  'ngResource',
  'ngRoute',
  'ngSanitize',
  'ngTable',
  'ngTouch',
  'nvd3',
  'picardy.fontawesome',
  'restangular',
  'slick',
  'toastr',
  'ui.bootstrap',
  'ui.bootstrap.modal',
  'ui.select',
  //'angularDc',
  //'stpa.morris',
]);

app.config(

  ['$routeProvider', '$locationProvider', 'toastrConfig', "environmentProvider",

    function($routeProvider, $locationProvider, toastrConfig, environmentProvider) {

      $routeProvider
        .when("/", {
          templateUrl: "app/homepage/homepage.template.html",
          controller: "HomepageCtrl",
        })
        .when("/portfolios", {
          templateUrl: "app/portfolios/_portfolios.template.html",
          controller: "PortfoliosCtrl"
        })
        .when("/portfolios/details/:portfolioId", {
          templateUrl: "app/portfolios/portfolios.template.html",
          controller: "PortfoliosCtrl"
        })
        .when("/screeners", {
          templateUrl: "app/screeners/screeners.template.html",
          controller: "ScreenersCtrl"
        })
        .when("/login", {
          templateUrl: "app/login/login.template.html",
          controller: "LoginCtrl"
        })
        .when("/register", {
          templateUrl: "app/register/register.template.html",
          controller: "RegisterCtrl"
        })
        .when("/settings", {
          templateUrl: "app/settings/settings.template.html",
          controller: "SettingsCtrl"
        })
        .when("/help", {
          templateUrl: "app/help/help.template.html",
          controller: "HelpCtrl"
        })
        .when("/contact", {
          templateUrl: "app/contact/contact.template.html",
          controller: "ContactCtrl"
        })
        .when("/admin", {
          templateUrl: "app/admin/admin.template.html",
          controller: "AdminCtrl"
        })
        .when("/doc", {
          controller: function() {
            window.location.replace('/doc');
          },
          template: "<div></div>"
        })
        .otherwise({
          redirectTo: "/"
        });

      $locationProvider
        .html5Mode({
          enabled: false
        });
      // todo : enable hashPrefix (SEO friendly)
      //.hashPrefix('!');


      angular.extend(toastrConfig, {
        allowHtml: false,
        closeButton: false,
        closeHtml: '<button>&times;</button>',
        containerId: 'toast-container',
        extendedTimeOut: 1000,
        iconClasses: {
          error: 'toast-error',
          info: 'toast-info',
          success: 'toast-success',
          warning: 'toast-warning'
        },
        maxOpened: 0,
        messageClass: 'toast-message',
        newestOnTop: true,
        onHidden: null,
        onShown: null,
        positionClass: 'toast-bottom-right',
        preventDuplicates: false,
        tapToDismiss: true,
        target: 'body',
        timeOut: 5000,
        titleClass: 'toast-title',
        toastClass: 'toast'
      });


      environmentProvider.setList(
        [{
          environment: 'prod',
          appPort: '80',
          backendPort: '80',
          titleTag: "",
          hasSubDomain: true,
        }, {
          environment: 'dev',
          appUrl: "localhost",
          appPort: '3000',
          backendPort: '3000', // gulp proxy automatically routes /api requests to port 8080
          titleTag: "-dev",
          hasSubDomain: false,
        }]
      );
      environmentProvider.setDefaultSubDomain("en");
    }
  ]
);

'use strict';

angular.module('squirrel').controller('BodyController',

  ["$scope", "$location", "layout",

    function($scope, $location, layout) {
      $scope.classFullPage = function() {
        if (layout.isFullPage()) {
          console.log("yes is full size!");
          return "view-full-page";
        }
        console.log("no full size");
        return "";
      }
    }
  ]
);
