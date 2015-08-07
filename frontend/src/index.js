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
  'ui.grid',
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
    }
  ]
);


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


angular.module('squirrel').run(

  ['$anchorScroll',

    function($anchorScroll) {
      $anchorScroll.yOffset = 80; // always scroll by 80 extra pixels
    }

  ]

)


/**
 * The following constant DEPLOYMENT.MODE will be set to 'dev' when serving with 'gulp serve', and
 * to 'prod' when the files has been built with gulp built and are serve by a production HTML
 * server.
 */
angular.module('squirrel').constant('DEPLOYMENT', {

  /**
   * Please keep exactly like this: 'MODE: "dev"' !!
   */
  MODE: "dev"

})


angular.module('squirrel').run(

  ['environment', 'request', 'debug', "DEPLOYMENT", "$rootScope",

    function(environment, request, debug, DEPLOYMENT, $rootScope) {
      if (DEPLOYMENT.MODE == "dev") {
        debug.debug("index", "getting features");
      }

      request.request("/api/features").then(function(data) {
        var environments = {
          "dev": {
            name: 'dev',
            appUrl: 'localhost',
            appPort: '3000',
            hasSubDomain: false,
            features: data,
          },
          "prod": {
            name: 'prod',
            appUrl: 'squirrel-ams.com',
            appPort: '80',
            hasSubDomain: false,
            features: data,
          }
        };
        /*
        if (DEPLOYMENT.MODE == "dev") {
          debug.dump("index", environments, "environment");
          debug.dump("index", DEPLOYMENT.MODE, "DEPLOYMENT.MODE");
          debug.dump("index", environments[DEPLOYMENT.MODE], "environments[DEPLOYMENT.MODE]");
        }
        */
        environment.setEnvironment(environments[DEPLOYMENT.MODE]);
        if (!environment.getFeatures().debug.logging) {
          /*debug.debug("index", "disabling debug level");*/
          debug.disable();
        }
        /* From here 'debug' service is configured */
        debug.dump("index", environment.getEnvironment(), "current environment: ");
        $rootScope.$broadcast(environment.ENVIRONMENT_FOUND);
      });
    }
  ]
)
