var app;

app = angular.module("squirrel", ['ngAnimate', 'ngCookies',
  'ngTouch', 'ngSanitize',
  'ngResource', 'ngRoute',
  'ui.bootstrap'
]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "app/main/main.template.html",
      controller: "MainCtrl"
    })
    .when("/info", {
      templateUrl: "app/info/info.template.html",
      controller: "InfoCtrl"
    })
    .when("/contact", {
      templateUrl: "app/contact/contact.template.html",
      controller: "ContactCtrl"
    })
    .when("/doc", {
      controller : function() {
        window.location.replace('/doc');
      },
      template : "<div></div>"
    })
    .otherwise({
      redirectTo: "/"
    });

  $locationProvider.html5Mode({
    enabled: false,
  });
}]);
