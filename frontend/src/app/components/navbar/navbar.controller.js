'use strict';

angular.module('squirrel').controller('NavbarCtrl',

  ["$scope", "$location", "$rootScope", "AuthenticationService", "Session", "AUTH_EVENTS",
   "gettextCatalog", "TranslationService", "environment", "debug",

    function($scope, $location, $rootScope, AuthenticationService, Session, AUTH_EVENTS,
      gettextCatalog, TranslationService, environment, debug) {

      $scope.date = new Date();
      $scope.login_username = "";
      $scope.is_admin = Session.isAdmin();
      $scope.currentLang = TranslationService.getCurrentLang();
      $scope.multilanguage = false;
      $scope.title_tag = "";
      $scope.navLinks = [];
      $scope.loginLinks = [];

      $scope.refreshDynamicLinks = function() {
        debug.debug("navbar", "refreshDynamicLinks");
        var is_logged = AuthenticationService.isAuthenticated();
        var features = environment.getFeatures();
        if (is_logged) {
          $scope.navLinks = [
            {
              endpoint: 'screeners',
              linktext: gettextCatalog.getString('Screeners'),
              state: features.screeners_page,
            }, {
              /*endpoint: 'portfolios?p=overview',*/
              endpoint: 'portfolios',
              linktext: gettextCatalog.getString('My Portfolios'),
              state: features.portfolio_page,
            }
          ];

          $scope.loginLinks = [];
        } else {
          // is unlogged user
          $scope.navLinks = [
            {
              endpoint: 'features',
              linktext: gettextCatalog.getString('Features'),
              state: features.features_page,
            }, {
              endpoint: 'plans',
              linktext: gettextCatalog.getString('Plans'),
              state: features.plans_page,
            }, {
              endpoint: 'screeners',
              linktext: gettextCatalog.getString('Screeners'),
              state: features.screeners_page,
            }, {
              endpoint: 'portfolios',
              linktext: gettextCatalog.getString('Demo'),
              state: features.demo_page,
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
        }
      };

      $rootScope.$on(environment.ENVIRONMENT_FOUND, function(event) {
        debug.debug("navbar", "on event: ENVIRONMENT_FOUND");
        $scope.multilanguage = (environment.getFeatures().languages.multilanguage == "enabled");
        $scope.title_tag = environment.getTitleTag();
        $scope.refreshDynamicLinks();
      });

      $rootScope.$on(TranslationService.TRANSLATION_UPDATED, function(event, lang) {
        debug.debug("navbar", "navbar on translation updated:" + lang);
        $scope.currentLang = TranslationService.getCurrentLang();
        $scope.refreshDynamicLinks();
      });

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        $scope.login_username = AuthenticationService.getFirstName();
        debug.debug("navbar", "navbar on loginSuccesful1:" + $scope.login_username);
        $scope.is_admin = Session.isAdmin();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        debug.debug("navbar", "navbar on logout");
        $scope.login_username = "";
        $scope.is_admin = false;
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        debug.debug("navbar", "navbar on loginError:" + error);
        $scope.login_username = "";
        $scope.is_admin = false;
      });

      $scope.logout = function() {
        debug.debug("navbar", "log out !!!");
        AuthenticationService.logout();
        $scope.closeNavBar();
      }

      $scope.active = function(page) {
        /*debug.debug("navbar", "location: " + $location.path() + ", page: " + page);*/
        if ($location.path() === "/" && page === '') {
          /*debug.debug("navbar", "returning active!")*/
          return true;
        }
        var currentRoute = $location.path().substring(1) || '/';
        return page === currentRoute ? true : false;
      };

      $scope.changeLang = function() {
        $scope.closeNavBar();
        TranslationService.askUserLanguage();
      };

      $scope.goRegister = function() {
        debug.debug("navbar", "goRegister");
        $scope.closeNavBar();
        $location.path("/register")
      };
      $scope.goLogin = function() {
        debug.debug("navbar", "goLogin");
        $scope.closeNavBar();
        $location.path("/login")
      };

      $scope.closeNavBar = function() {
        $scope.navCollapsed = true;
      }
    }
  ]
);
