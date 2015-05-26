'use strict';

angular.module('squirrel').filter('json_currency', function() {

  return function(json_data) {
    var output;
    if (json_data.c == "euro") {
      output = json_data.v + " €";
    } else if (json_data.c == "dollar") {
      output = "$ " + json_data.v;
    }
    return output;
  }
});
