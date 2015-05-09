'use strict';

var app;

// we use lodash is better than undercore: http: //kitcambridge.be/blog/say-hello-to-lo-dash/
app = angular.module("squirrel", [
  // keep the following lines sorted!
  'angular-parallax',
  'angular-timeline',
  'angularModalService',
  'angularMoment',
  'ct.ui.router.extras',
  'duScroll',
  'gettext',
  'highcharts-ng',
  'ipCookie',
  'Mac',
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
  'sun.scrollable',
  'toastr',
  'ui.bootstrap',
  'ui.bootstrap.modal',
  'ui.router',
  'ui.select',
  //'angularDc',
  //'stpa.morris',
]);

app.config(

  ['$routeProvider', '$locationProvider', 'toastrConfig', "environmentProvider",
  "$stateProvider", "$urlRouterProvider",

    function($routeProvider, $locationProvider, toastrConfig, environmentProvider,
      $stateProvider, $urlRouterProvider) {
      $urlRouterProvider.otherwise("/");

      $stateProvider
        .state('homepage', {
          url: "/",
          templateUrl: "app/homepage/homepage.template.html",
          controller: "HomepageCtrl",
        })
        .state('portfolios', {
          url: "/portfolios",
          templateUrl: "app/portfolios/_portfolios.template.html",
          controller: "PortfoliosCtrl",
          reloadOnSearch: false
        })
        .state('screeners', {
          url: "/screeners",
          templateUrl: "app/screeners/screeners.template.html",
          controller: "ScreenersCtrl",
        })
        .state('login', {
          url: "/login",
          templateUrl: "app/login/login.template.html",
          controller: "LoginCtrl",
        })
        .state('register', {
          url: "/register",
          templateUrl: "app/register/register.template.html",
          controller: "RegisterCtrl",
        })
        .state('settings', {
          url: "/settings",
          templateUrl: "app/settings/settings.template.html",
          controller: "SettingsCtrl",
        })
        .state('help', {
          url: "/help",
          templateUrl: "app/help/help.template.html",
          controller: "HelpCtrl",
        })
        .state("admin", {
          url: "/admin",
          templateUrl: "app/admin/_admin.template.html",
          controller: "AdminCtrl",
          reloadOnSearch: false
        })
        .state("sandbox", {
          url: "/sandbox",
          templateUrl: "app/sandbox/_sandbox.template.html",
          controller: "SandboxCtrl",
          reloadOnSearch: false
        })
        .state("tos", {
          url: "/tos",
          templateUrl: "app/pages/tos.template.html",
          controller: "TosCtrl"
        })
        .state("features", {
          url: "/features",
          templateUrl: "app/pages/features.template.html",
          controller: "FeaturesCtrl"
        })
        .state("plans", {
          url: "/plans",
          templateUrl: "app/pages/plans.template.html",
          controller: "PlansCtrl"
        })
        .state("security", {
          url: "/security",
          templateUrl: "app/pages/security.template.html",
          controller: "SecurityCtrl"
        })
        .state("contact", {
          url: '/contact',
          templateUrl: "app/contact/contact.template.html",
          controller: "ContactCtrl"
        });
      /*
            $routeProvider
              .when("/", {
                templateUrl: "app/homepage/homepage.template.html",
                controller: "HomepageCtrl",
              })
              .when("/portfolios", {
                templateUrl: "app/portfolios/_portfolios.template.html",
                controller: "PortfoliosCtrl",
                reloadOnSearch: false
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
                templateUrl: "app/admin/_admin.template.html",
                controller: "AdminCtrl",
                reloadOnSearch: false
              })
              .when("/sandbox", {
                templateUrl: "app/sandbox/_sandbox.template.html",
                controller: "SandboxCtrl",
                reloadOnSearch: false
              })
              .when("/tos", {
                templateUrl: "app/pages/tos.template.html",
                controller: "TosCtrl"
              })
              .when("/features", {
                templateUrl: "app/pages/features.template.html",
                controller: "FeaturesCtrl"
              })
              .when("/plans", {
                templateUrl: "app/pages/plans.template.html",
                controller: "PlansCtrl"
              })
              .when("/security", {
                templateUrl: "app/pages/security.template.html",
                controller: "SecurityCtrl"
              })
              .when("/doc", {
                controller: function() {
                  window.location.replace('/doc');
                },
                template: "<div></div>"
              })
              .otherwise({
                redirectTo: "/"
              });*/

      $locationProvider
        .html5Mode({
          enabled: true,
          requireBase: true
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
          /*console.log("yes is full size!");*/
          return "view-full-page";
        }
        /*console.log("no full size");*/
        return "";
      }
    }
  ]
);

angular.module('squirrel').run(['$anchorScroll', function($anchorScroll) {
  $anchorScroll.yOffset = 80; // always scroll by 80 extra pixels
}])
