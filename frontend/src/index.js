'use strict';

var app;

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
  'underscore',
  'picardy.fontawesome',
  'toaster',
]);

app.config(

  ['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider) {

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

      $locationProvider.html5Mode({
        enabled: false,
      });
    }
  ]
);
