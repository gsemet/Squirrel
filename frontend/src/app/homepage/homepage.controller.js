'use strict';

angular.module('squirrel').controller('HomepageCtrl',

  ["AuthenticationService", "$rootScope", '$scope', "AUTH_EVENTS", "request", "TranslationService",
    "$timeout", "$location", "$document",

    function(AuthenticationService, $rootScope, $scope, AUTH_EVENTS, request, TranslationService,
      $timeout, $location, $document) {

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

      $scope.signup = function() {
        $location.path("/register");
      }
    }
  ]
);
