'use strict';


angular.module('squirrel').factory('TranslationService',

  ['gettextCatalog', "AUTH_EVENTS", "$rootScope", "AuthenticationService", "ipCookie", "ModalService",
    "$timeout", "DEPLOYMENT", "debug", "$location",

    function(gettextCatalog, AUTH_EVENTS, $rootScope, AuthenticationService, ipCookie, ModalService,
      $timeout, DEPLOYMENT, debug, $location) {

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
        debug.info("TranslationService", "translation service on loginSuccesful: " + userName);
        var lang = AuthenticationService.getUserLanguage();
        debug.info("TranslationService", " lang => " + lang);
        ipCookie("prefered-language", lang);
        translationService.setLangFromCookie();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        debug.info("TranslationService", "translation service on logout");
        translationService.setLangFromCookie();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        debug.info("TranslationService", "translation service on loginError:" + error);
      });

      translationService.setLangFromCookie = function() {
        var lang = ipCookie("prefered-language");
        if (lang && lang != 'us') {
          debug.info("TranslationService", "Setting current language to " + lang +
            ", mode=" + DEPLOYMENT.MODE);
          gettextCatalog.setCurrentLanguage(lang);
          if (DEPLOYMENT.MODE == 'dev') {
            debug.info("TranslationService", "debug mode enabled");
            gettextCatalog.debug = true;
          }
          translationService.currentLang = lang;
          translationService.setExternalToolLang();
          $rootScope.$emit(translationService.TRANSLATION_UPDATED, lang);
          debug.info("TranslationService", "emiting signal = TRANSLATION_UPDATED " + lang);
        } else {
          gettextCatalog.setCurrentLanguage('en');
          debug.info("TranslationService", "Setting to default language 'us' (='en')");
          if (!lang) {
            translationService.currentLang = 'en';
            $timeout(function() {
              translationService.setLangFromDomain();
            }, 100);
          } else {
            translationService.currentLang = lang;
            translationService.setExternalToolLang();
            debug.info("TranslationService", "emiting signal = TRANSLATION_UPDATED " + lang);
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
            debug.info("TranslationService", "You said you wanted language: " + lang);
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

      translationService.setLangFromDomain = function() {
        var domain = translationService.getcurrentDomain();
        debug.dump("TranslationService", domain, "Setting language from domain:");
        if (domain == "fr") {
          ipCookie("prefered-language", "fr");
          translationService.setLangFromCookie();
        } else if (domain == "en") {
          ipCookie("prefered-language", "us");
          translationService.setLangFromCookie();
        } else {
          ipCookie("prefered-language", "us");
          translationService.setLangFromCookie();
        }
      }

      translationService.getcurrentDomain = function() {
        var matches;
        var output = "";
        var urls = /\w+:\/\/([\w|\.]+)/;

        matches = urls.exec($location.host());

        if (matches !== null) {
          output = matches[1];
        }

        return output;
      }

      translationService.getCurrentLanguage = function() {
        debug.info("TranslationService", "translationService.currentLang = " +
          JSON.stringify(translationService.currentLang));
        var found = null;
        _.forEach(translationService.languages, function(lang) {
          debug.info("TranslationService", "lang = " + JSON.stringify(lang) + "?");
          if (translationService.currentLang == lang.short_lang) {
            debug.info("TranslationService", "returing = " + JSON.stringify(lang.language));
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
