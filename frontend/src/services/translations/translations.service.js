'use strict';


angular.module('squirrel').factory('TranslationService',

  ['gettextCatalog', "AUTH_EVENTS", "$rootScope", "AuthenticationService", "ipCookie", "ModalService",
    "$timeout",

    function(gettextCatalog, AUTH_EVENTS, $rootScope, AuthenticationService, ipCookie, ModalService,
      $timeout) {

      var translationService = {};

      translationService.TRANSLATION_UPDATED = "translation_updated";

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("translation service on loginSuccesful:" + userName);
        var lang = AuthenticationService.getUserLanguage();
        gettextCatalog.setCurrentLanguage(lang);
        ipCookie("prefered-language", lang);
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("translation service on logout");
        translationService.setLangFromCookie();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("translation service on loginError:" + error);
      });

      translationService.setLangFromCookie = function() {
        var lang = ipCookie("prefered-language");
        if (lang && lang != 'en') {
          console.log("Setting current language to " + lang);
          gettextCatalog.setCurrentLanguage(lang);
          gettextCatalog.debug = true;
          translationService.currentLang = lang;
        } else {
          gettextCatalog.setCurrentLanguage('en');
          console.log("Setting to default language 'en'");
          if (!lang) {
            translationService.currentLang = null;
            $timeout(function() {
              translationService.askUserLanguage();
            }, 1000);
          } else {
            translationService.currentLang = lang;
          }
          gettextCatalog.debug = false;
        }
      };

      translationService.askUserLanguage = function() {
        // Ex:
        //     http://jsfiddle.net/dwmkerr/8MVLJ/
        ModalService.showModal({
          templateUrl: "services/translations/get_translation.modal.template.html",
          controller: "GetTranslationController"
        }).then(function(modal) {
          // The modal object has the element built, if this is a bootstrap modal
          // you can call 'modal' to show it, if it's a custom modal just show or hide
          // it as you need to.
          modal.element.modal();
          modal.close.then(function(lang) {
            console.log("You said you wanted language: " + lang);
            if (lang) {
              ipCookie("prefered-language", lang);
              translationService.setLangFromCookie();
              $rootScope.$emit(translationService.TRANSLATION_UPDATED, lang);
            }
          });
        });
      };


      translationService.getCurrentLang = function() {
        return translationService.currentLang;
      };

      return translationService;
    }
  ]
);


angular.module('squirrel').run(

  ["TranslationService",

    function(TranslationService) {

      TranslationService.setLangFromCookie();

    }
  ]
);
