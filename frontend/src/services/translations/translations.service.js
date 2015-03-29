'use strict';

angular.module('squirrel').run(

  ['gettextCatalog',

    function(gettextCatalog) {
      gettextCatalog.setCurrentLanguage('fr');
      gettextCatalog.debug = true;
    }
  ]
);
