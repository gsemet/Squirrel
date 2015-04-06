'use strict';

var app;

// we use lodash is better than undercore: http: //kitcambridge.be/blog/say-hello-to-lo-dash/
app = angular.module("squirrel", [
  'duScroll',
  'duParallax',
  'angular-parallax',
  "highcharts-ng",
  'ipCookie',
  'ngAnimate',
  'ngCookies',
  'ngResource',
  'ngRoute',
  'ngSanitize',
  'ngTouch',
  'ui.bootstrap',
  'ui.bootstrap.modal',
  'picardy.fontawesome',
  'toastr',
  'ngGrid',
  'gettext',
  'ngCrossfilter',
  'angular-timeline',
  'stpa.morris',
  'nvd3',
  'angularDc',
  'angularMoment',
  'restangular',
  'angularModalService',
  'mgcrea.ngStrap',
  'ui.select',
]);

app.config(

  ['$routeProvider', '$locationProvider', 'toastrConfig',

    function($routeProvider, $locationProvider, toastrConfig) {

      $routeProvider
        .when("/", {
          templateUrl: "app/homepage/homepage.template.html",
          controller: "HomepageCtrl",
        })
        .when("/my-portfolios", {
          templateUrl: "app/my-portfolios/my-portfolios.template.html",
          controller: "MyPortfoliosCtrl"
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
    }
  ]
);
