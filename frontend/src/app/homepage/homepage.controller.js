'use strict';

angular.module('squirrel').controller('HomepageCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS", "request", "TranslationService",
    "$timeout", "$location", "$document", "gettextCatalog",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS, request, TranslationService,
      $timeout, $location, $document, gettextCatalog) {

      $document.scrollTo(0, 0);

      $scope.logged_in = AuthenticationService.isAuthenticated();

      $rootScope.$on(TranslationService.TRANSLATION_UPDATED, function(event, lang) {
        $scope.refreshAccounts();
      });

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("homepage on loginSuccesful1:" + userName);
        $scope.logged_in = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("homepage on logout");
        $scope.logged_in = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("homepage on loginError:" + error);
        $scope.logged_in = false;
      });

      $scope.refreshAccounts = function() {
        console.log("received marketing request");
        var lang = TranslationService.getCurrentLang();
        request.request("/api/marketing?r=homepage-accounts&l=" + lang).then(function(data) {
          console.log("data = " + JSON.stringify(data));
          $scope.accounts = data;
        });
      };

      $timeout($scope.refreshAccounts, 500);

      $scope.parallaxText = gettextCatalog.getString("Squirrel is the simpler, yet most powerful " +
        "online portfolio management tool. It allows " +
        "a private individual to grab easily its investment decisions.It efficiently replaces " +
        "custom - made spreadsheet and provides state of the art graphical visualization tools.");

      $scope.signup = function() {
        $location.path("/register");
      }
    }
  ]
);
