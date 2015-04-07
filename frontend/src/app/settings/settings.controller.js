'use strict';

angular.module("squirrel").controller("SettingsCtrl",

  ["$scope", "TranslationService", "$rootScope", "$timeout", "AuthenticationService", "AUTH_EVENTS",

    function($scope, TranslationService, $rootScope, $timeout, AuthenticationService, AUTH_EVENTS) {

      $scope.logged_in = AuthenticationService.isAuthenticated();

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("settings on loginSuccesful1:" + userName);
        $scope.logged_in = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("settings on logout");
        $scope.logged_in = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("settings on loginError:" + error);
        $scope.logged_in = false;
      });

      $scope.refresh = function() {
        $scope.language = TranslationService.getCurrentLanguage();
      };
      $timeout($scope.refresh, 300);

      $scope.changeLang = function() {
        TranslationService.askUserLanguage();
      };

      $rootScope.$on(TranslationService.TRANSLATION_UPDATED, function(event, lang) {
        $scope.refresh();
      });
    }
  ]
);
