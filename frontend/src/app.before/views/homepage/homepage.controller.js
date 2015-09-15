'use strict';

class HomepageController {
  constructor($rootScope, $timeout, TranslationService, request, gettextCatalog,
      AuthenticationService, $document) {
      'ngInject';

      this.parallaxText = gettextCatalog.getString("Squirrel is the simpler, yet most powerful " +
        "online portfolio management tool. It allows " +
        "a private individual to grab easily its investment decisions.It efficiently replaces " +
        "custom - made spreadsheet and provides state of the art graphical visualization tools.");

      this.logged_in = AuthenticationService.isAuthenticated();

      $timeout(this.refreshAccounts, 500);

      /*this.registerEvents();*/

      $document.scrollTo(0, 0);
    }
    /*
      registerEvents() {

        $rootScope.$on(TranslationService.TRANSLATION_UPDATED, function(event, lang) {
          this.refreshAccounts();
        });

        $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
          console.log("homepage on loginSuccesful1:" + userName);
          this.logged_in = AuthenticationService.isAuthenticated();
        });

        $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
          console.log("homepage on logout");
          this.logged_in = false;
        });

        $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
          console.log("homepage on loginError:" + error);
          this.logged_in = false;
        });
      }

      refreshAccounts() {
        var lang = TranslationService.getCurrentLang();
        request.request("/api/marketing?r=homepage-accounts&l=" + lang).then(function(data) {
          this.accounts = data;
        });
      };

      signup($location) {
        $location.path("/register");
      }*/
}

export default HomepageController;
