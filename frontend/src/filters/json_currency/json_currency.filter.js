'use strict';

angular.module('squirrel').filter('json_currency', function() {

  return function(json_data) {
    var output;
    output = json_data.v + " " + json_data.c;
    return output;
  }
});
