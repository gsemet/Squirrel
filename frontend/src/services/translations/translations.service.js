'use strict';


angular.module('squirrel').factory('TranslationService',

  ['gettextCatalog', "AUTH_EVENTS", "$rootScope", "AuthenticationService", "ipCookie", "ModalService",
    "$timeout", "DEPLOYMENT",

    function(gettextCatalog, AUTH_EVENTS, $rootScope, AuthenticationService, ipCookie, ModalService,
      $timeout, DEPLOYMENT) {

      var translationService = {
        languages: [{
          'language': 'French (France)',
          'short_lang': 'fr'
        }, {
          'language': 'English (US)',
          'short_lang': 'us'
        }],
        TRANSLATION_UPDATED: "translation_updated",
      };

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("translation service on loginSuccesful: " + userName);
        var lang = AuthenticationService.getUserLanguage();
        console.log(" lang => " + lang);
        ipCookie("prefered-language", lang);
        translationService.setLangFromCookie();
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
        if (lang && lang != 'us') {
          console.log("Setting current language to " + lang + "mode=" + DEPLOYMENT.MODE);
          gettextCatalog.setCurrentLanguage(lang);
          if (DEPLOYMENT.MODE == 'dev') {
            console.log("debug mode enabled");
            gettextCatalog.debug = true;
          }
          translationService.currentLang = lang;
          translationService.setExternalToolLang();
          $rootScope.$emit(translationService.TRANSLATION_UPDATED, lang);
          console.log("emiting signal = TRANSLATION_UPDATED " + lang);
        } else {
          gettextCatalog.setCurrentLanguage('en');
          console.log("Setting to default language 'us' (='en')");
          if (!lang) {
            translationService.currentLang = null;
            $timeout(function() {
              translationService.askUserLanguage();
            }, 1000);
          } else {
            translationService.currentLang = lang;
            translationService.setExternalToolLang();
            console.log("emiting signal = TRANSLATION_UPDATED " + lang);
            $rootScope.$emit(translationService.TRANSLATION_UPDATED, lang);

          }
          gettextCatalog.debug = false;
        }
      };

      translationService.askUserLanguage = function() {
        // Ex:
        //     http://jsfiddle.net/dwmkerr/8MVLJ/
        ModalService.showModal({
          templateUrl: "services/translations/get_translation.modal.template.html",
          controller: "GetTranslationController",
          inputs: {
            languages: translationService.languages,
            currentLang: translationService.currentLang
          }
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

      translationService.getCurrentLanguage = function() {
        console.log("translationService.currentLang = " + JSON.stringify(translationService.currentLang));
        var found = null;
        _.forEach(translationService.languages, function(lang) {
          console.log("lang = " + JSON.stringify(lang) + "?");
          if (translationService.currentLang == lang.short_lang) {
            console.log("returing = " + JSON.stringify(lang.language));
            found = lang.language;
          };
        });
        return found;
      };

      translationService.setExternalToolLang = function() {
        Highcharts.setOptions({
          lang: {
            loading: gettextCatalog.getString('Loading...'),
            months: [
              gettextCatalog.getString('January'),
              gettextCatalog.getString('February'),
              gettextCatalog.getString('March'),
              gettextCatalog.getString('April'),
              gettextCatalog.getString('May'),
              gettextCatalog.getString('June'),
              gettextCatalog.getString('July'),
              gettextCatalog.getString('August'),
              gettextCatalog.getString('September'),
              gettextCatalog.getString('October'),
              gettextCatalog.getString('November'),
              gettextCatalog.getString('December')
            ],
            shortMonths: [
              gettextCatalog.getString('Jan'),
              gettextCatalog.getString('Feb'),
              gettextCatalog.getString('Mar'),
              gettextCatalog.getString('Apr'),
              gettextCatalog.getString('May'),
              gettextCatalog.getString('Jun'),
              gettextCatalog.getString('Jul'),
              gettextCatalog.getString('Aug'),
              gettextCatalog.getString('Sep'),
              gettextCatalog.getString('Oct'),
              gettextCatalog.getString('Nov'),
              gettextCatalog.getString('Dec')
            ],
            weekdays: [
              gettextCatalog.getString('Sunday'),
              gettextCatalog.getString('Monday'),
              gettextCatalog.getString('Tuesday'),
              gettextCatalog.getString('Wednesday'),
              gettextCatalog.getString('Thursday'),
              gettextCatalog.getString('Friday'),
              gettextCatalog.getString('Saturday')
            ],
            /// decimal point
            decimalPoint: gettextCatalog.getString('.'),
            numericSymbols: ['k', 'M', 'G', 'T', 'P', 'E'], // SI prefixes used in axis labels
            resetZoom: gettextCatalog.getString('Reset zoom'),
            resetZoomTitle: gettextCatalog.getString('Reset zoom level 1:1'),
            /// thousands separator
            thousandsSep: gettextCatalog.getString(','),
            rangeSelectorZoom: gettextCatalog.getString('Zoom'),
            rangeSelectorFrom: gettextCatalog.getString('From'),
            rangeSelectorTo: gettextCatalog.getString('To')
          }
        });
      }
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
