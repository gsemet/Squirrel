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
  'toastr',
  'ui.bootstrap',
  'ui.bootstrap.modal',
  'ui.select',
  //'angularDc',
  //'stpa.morris',
]);

app.config(

  ['$routeProvider', '$locationProvider', 'toastrConfig',

    function($routeProvider, $locationProvider, toastrConfig) {

      $routeProvider
        .when("/", {
          templateUrl: "app/homepage/homepage.template.html",
          controller: "HomepageCtrl",
        })
        .when("/portfolios", {
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
    }
  ]
);
