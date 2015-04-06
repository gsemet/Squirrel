'use strict';

angular.module('squirrel').controller('GetTranslationController',

  ['$scope', 'close',

    function($scope, close) {

      $scope.language = {};
      $scope.languages = [];
      $scope.languages.push({
        'language': 'French (France)',
        'short_lang': 'fr'
      }, {
        'language': 'English (US)',
        'short_lang': 'en'
      });

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
