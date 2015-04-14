'use strict';

angular.module('squirrel').controller('GetTranslationController',

  ['$scope', 'close', "languages", "currentLang",

    function($scope, close, languages, currentLang) {

      $scope.languages = languages;

      $scope.language = {};
      console.log("currentLang = " + JSON.stringify(currentLang));
      if (currentLang) {
        _.forEach($scope.languages, function(item) {
          console.log("item = " + JSON.stringify(item));
          console.log("item.short_lang = " + JSON.stringify(item.short_lang));
          if (item.short_lang == currentLang) {
            $scope.language = {
              selected: item
            };
          }
        });
      }

      $scope.ok = function() {
        if ($scope.language.selected) {
          close($scope.language.selected.short_lang, 500); // close, but give 500ms for bootstrap to animate
        } else {
          close(null, 500); // close, but give 500ms for bootstrap to animate
        }
      };

      $scope.cancel = function() {
        close(null, 500); // close, but give 500ms for bootstrap to animate
      };
    }
  ]
);
