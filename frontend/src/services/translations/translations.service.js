'use strict';

angular.module('squirrel').run(

  ['gettextCatalog', "AUTH_EVENTS", "$rootScope", "AuthenticationService", "ipCookie", "ModalService", "$modal",

    function(gettextCatalog, AUTH_EVENTS, $rootScope, AuthenticationService, ipCookie, ModalService, $modal) {

      var that = {};

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        console.log("translation service on loginSuccesful:" + userName);
        var lang = AuthenticationService.getUserLanguage();
        gettextCatalog.setCurrentLanguage(lang);
        ipCookie("prefered-language", lang);
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        console.log("translation service on logout");
        that.setLangFromCookie();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        console.log("translation service on loginError:" + error);
      });

      that.setLangFromCookie = function() {
        var lang = ipCookie("prefered-language");
        if (lang && lang != 'en') {
          console.log("Setting current language to " + lang);
          gettextCatalog.setCurrentLanguage(lang);
          gettextCatalog.debug = true;
        } else {
          gettextCatalog.setCurrentLanguage('en');
          console.log("Setting to default language 'en'");
          gettextCatalog.debug = false;
          setTimeout(function() {
            that.askUserLanguage();
          }, 1000);
        }
      };

      that.askUserLanguage = function() {
        /* console.log("askUserLanguage");
          var myOtherModal = $modal({
            template: 'services/translations/get_translation.modal.template.html',
            show: true
          });*/
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
              that.setLangFromCookie();
            }
          });
        });
      }

      that.setLangFromCookie();
    }
  ]
);
