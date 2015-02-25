angular.module "squirrel", ['ngAnimate', 'ngCookies', 'ngTouch', 'ngSanitize', 'ngResource', 'ngRoute', 'ui.bootstrap']
  .config ($routeProvider) ->
    $routeProvider
      .when "/",
        templateUrl: "app/main/main.html"
        controller: "MainCtrl"
      .when "/info",
        templateUrl: "app/info/info.html"
        controller: "InfoCtrl"
      .when "/contact",
        templateUrl: "app/contact/contact.html"
        controller: "ContactCtrl"
      .otherwise
        redirectTo: "/"

