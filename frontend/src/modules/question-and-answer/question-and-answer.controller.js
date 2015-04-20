'use strict';

angular.module('squirrel').controller('QuestionAndAnswerCtrl',

  ["$scope", "gettextCatalog",

    function($scope, gettextCatalog) {
      $scope.expand = false;
    }
  ]
);
