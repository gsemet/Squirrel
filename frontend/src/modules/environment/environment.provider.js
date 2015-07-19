'use strict';

angular.module('squirrel').factory('environment',

  ['debug',

    function(debug) {

      // DEFAULT
      var environment = {
        env: {},
      };

      environment.getEnvironment = function() {
        return environment.env;
      };

      environment.getAppUrl = function() {
        var env = environment.env;
        var currentSSL = (env.appUseSSL) ? 'https://' : 'http://';
        var currentAppUrl = (env.appUrl) ? env.appUrl : list.appUrl;
        var currentAppPort = (env.appPort) ? ':' + env.appPort : '';

        return currentSSL + currentAppUrl + currentAppPort;
      };

      environment.getBackendUrl = function() {
        var env = environment.env;
        var currentSSL = (env.backendUseSSL) ? 'https://' : 'http://';
        var currentbackendUrl = (env.backendUrl) ? env.backendUrl : env.appUrl;
        var currentServicePort = (env.servicePort) ? ':' + env.servicePort : '';

        currentServicePort = (!env.servicePort && !env.backendUrl) ? ':' + env.appPort : currentServicePort;

        return currentSSL + currentbackendUrl + currentServicePort;
      };

      environment.getTitleTag = function() {
        var env = environment.env;
        var titleTag = env.titleTag;
        if (titleTag) {
          return env.titleTag;
        } else {
          return "";
        }
      };

      environment.getFeatures = function() {
        var env = environment.env;
        var features = env.features;
        if (features) {
          return env.features;
        } else {
          return {};
        }
      };

      environment.getSubDomain = function() {
        var env = environment.env;
        if (env.hasSubDomain) {
          return null;
        }
        var host = $location.host();
        if (host.indexOf('.') < 0) {
          return this.defaultSubDomain;
        } else {
          return host.split('.')[0];
        }
      };

      environment.setEnvironment = function(env) {
        environment.env = env;
        debug.dump("environment", environment.env, "environment.env");
      };

      environment.ENVIRONMENT_FOUND = "environment_found";
      return environment;
    }

  ]

);
