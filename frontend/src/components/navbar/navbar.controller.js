'use strict';

angular.module('squirrel').controller('NavbarCtrl',

  ["$scope", "$location", "$rootScope", "AuthenticationService", "AUTH_EVENTS", "gettextCatalog", "TranslationService",

    function($scope, $location, $rootScope, AuthenticationService, AUTH_EVENTS, gettextCatalog, TranslationService) {

      $scope.date = new Date();
      $scope.login_username = "";
      $scope.is_admin = AuthenticationService.isAdmin();
      $scope.currentLang = TranslationService.getCurrentLang();

      $scope.refreshDynamicLinks = function() {
        $scope.navLinks = [
          {
            endpoint: 'screeners',
            linktext: gettextCatalog.getString('Stock Screeners'),
          }, {
            endpoint: 'my-portfolios',
            linktext: gettextCatalog.getString('My Portfolios'),
          }
        ];

        $scope.loginLinks = [
          {
            endpoint: 'login',
            linktext: gettextCatalog.getString('Login'),
          }, {
            endpoint: 'register',
            linktext: gettextCatalog.getString('Register'),
          }
        ];
      };
      $scope.refreshDynamicLinks();

      $rootScope.$on(TranslationService.TRANSLATION_UPDATED, function(event, lang) {
        console.log("navbar on translation updated:" + lang);
        $scope.currentLang = TranslationService.getCurrentLang();
        $scope.refreshDynamicLinks();
      });


      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("navbar on loginSuccesful1:" + userName);
        $scope.login_username = userName;
        $scope.is_admin = AuthenticationService.isAdmin();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("navbar on logout");
        $scope.login_username = "";
        $scope.is_admin = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("navbar on loginError:" + error);
        $scope.login_username = "";
        $scope.is_admin = false;
      });

      $scope.logout = function() {
        console.log("log out !!!");
        AuthenticationService.logout();
      }

      $scope.navClass = function(page) {
        /*console.log("location: " + $location.path() + ", page: " + page);*/
        if ($location.path() === "/" && page === '') {
          /*console.log("returning active!")*/
          return "active";
        }
        var currentRoute = $location.path().substring(1) || '/';
        return page === currentRoute ? 'active' : '';
      };

      $scope.changeLang = function() {
        TranslationService.askUserLanguage();
      };
    }
  ]
);
