'use strict';

angular.module("squirrel").filter('unsafe',

  function($sce) {

    return $sce.trustAsHtml;
  }
);
