'use strict';

angular.module('squirrel').directive('questionAndAnswer',

  [

    function() {
      return {
        replace: true,
        transclude: true,
        restrict: 'E',
        scope: {
          question: '@question',
        },
        controllerAs: "page",
        templateUrl: "modules/question-and-answer/question-and-answer.template.html",
        controller: "QuestionAndAnswerCtrl",
      };
    }
  ]
);
