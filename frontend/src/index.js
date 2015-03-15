var app;

app = angular.module("squirrel", ['ngAnimate', 'ngCookies',
  'ngTouch', 'ngSanitize',
  'ngResource', 'ngRoute',
  'ui.bootstrap'
]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "app/homepage/homepage.template.html",
      controller: "HomepageCtrl"
    })
    .when("/my-portfolios", {
      templateUrl: "app/my-portfolios/my-portfolios.template.html",
      controller: "MyPortfoliosCtrl"
    })
    .when("/screeners", {
      templateUrl: "app/screeners/screeners.template.html",
      controller: "ScreenersCtrl"
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
}]);
