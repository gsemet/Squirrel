'use strict';

angular.module('squirrel').factory('debug',

  ["$log",

    function($log) {

      this.debug_settings = [];
      var debug_service = {};

      debug_service.log = function(module, text) {
        $log.log("[" + module + "] " + text);
      };

      debug_service.warn = function(module, text) {
        $log.warn("%c [" + module + "] " + text,
          'background: #CF8902; color: #000000');
      };

      debug_service.info = function(module, text) {
        $log.info("%c [" + module + "] " + text,
          'color: #0006FF');
      };

      debug_service.error = function(module, text) {
        $log.error("%c [" + module + "] " + text,
          'background: #E20000; color: #FFFFFF');
      };

      debug_service.debug = function(module, text) {
        $log.debug("%c [" + module + "] " + text, 'background: #FFFFFF; color: #444444');
      };

      debug_service.dump = function(module, obj, name) {
        if (!name) {
          name = "Object"
        }
        $log.log("%c [" + module + "] " + name + ": " + JSON.stringify(obj),
          'background: #DFDFDF; color: #000000#000000');
      };

      return debug_service;
    }
  ]
);
