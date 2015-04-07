'use strict';

angular.module('squirrel').controller('GetTranslationController',

  ['$scope', 'close', "languages", "currentLang",

    function($scope, close, languages, currentLang) {

      $scope.languages = languages;

      $scope.language = {};
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
