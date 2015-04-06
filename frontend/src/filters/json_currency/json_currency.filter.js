'use strict';

angular.module('squirrel').filter('json_currency', function() {

  return function(json_data) {
    var output;
    output = json_data.value + " " + json_data.currency;
    return output;
  }
});
