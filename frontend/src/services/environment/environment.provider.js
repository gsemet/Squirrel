'use strict';

angular.module('squirrel').provider('environment',

  function() {

    // Defines different environments.
    //
    // The environment will be selected based on the url
    //
    // Example:
    //
    // environmentProvider.setList(
    //   [{
    //     environment: 'local',
    //     appUseSSL: false,
    //     appUrl: 'localhost',
    //     appPort: '9000', // only if using a non-standard port (80 or 443)
    //     backendUseSSL: false,
    //     backendUrl: 'myApp-dev.servercom' // optional: if different from appUrl,
    //     servicePort: '8080' // only if using a non-standard port (80 or 443)
    //   },
    //   {
    //     environment: 'dev',
    //     appUrl: 'myApp-dev.servercom'
    //   },
    //   {
    //     environment: 'preview',
    //     appUrl: 'myApp-pre.servercom'
    //   },
    //   {
    //     environment: 'prod',
    //     appUrl: 'subdomain.servercom/myAppVirtualDirectory'
    //   }]
    // );

    // DEFAULT
    this.list = [{
      environment: 'local',
      appUrl: 'localhost',
      appPort: '3000',
      hasSubDomain: false,
    }];
    this.defaultSubDomain = "";

    this.setList = function(list) {
      this.list = list;
    };

    this.setDefaultSubDomain = function(defaultSubDomain) {
      this.defaultSubDomain = defaultSubDomain;
    }


    this.$get = function($location) {
      var list = this.list;
      var host = $location.host();
      var env = null;

      var findCurrentEnvironment = function() {
        host = host.toLowerCase();

        if (!env && _.isArray(list) && list.length > 0) {
          console.log("searching env");
          env = _.find(list, function(environment) {
            console.log("evaluating = " + JSON.stringify(environment));
            if (environment.appUrl) {
              var lowercaseUrl = environment.appUrl.toLowerCase();
              return (lowercaseUrl == host);
            }
          });

          console.log("found env = " + JSON.stringify(env));

          if (!env) {
            //Environment not found fall back to a default.
            env = list[0];
          }
        }

        return env;
      };

      var getEnvironment = function() {
        var enviro = findCurrentEnvironment();
        console.log('enviro: ' + enviro);
        return (enviro) ? enviro.environment : 'local';
      };

      var getAppUrl = function() {
        var env = findCurrentEnvironment();
        var currentSSL = (env.appUseSSL) ? 'https://' : 'http://';
        var currentAppUrl = (env.appUrl) ? env.appUrl : list.appUrl;
        var currentAppPort = (env.appPort) ? ':' + env.appPort : '';

        return currentSSL + currentAppUrl + currentAppPort;
      };

      var getBackendUrl = function() {
        var env = findCurrentEnvironment();
        console.log("env = " + JSON.stringify(env));
        var currentSSL = (env.backendUseSSL) ? 'https://' : 'http://';
        var currentbackendUrl = (env.backendUrl) ? env.backendUrl : env.appUrl;
        var currentServicePort = (env.servicePort) ? ':' + env.servicePort : '';

        currentServicePort = (!env.servicePort && !env.backendUrl) ? ':' + env.appPort : currentServicePort;

        return currentSSL + currentbackendUrl + currentServicePort;
      };

      var getTitleTag = function() {
        var env = findCurrentEnvironment();
        var titleTag = env.titleTag;
        if (titleTag) {
          return env.titleTag;
        } else {
          return "";
        }
      };

      var getSubDomain = function() {
        var env = findCurrentEnvironment();
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

      return {
        getEnvironment: getEnvironment,
        getAppUrl: getAppUrl,
        getBackendUrl: getBackendUrl,
        getTitleTag: getTitleTag,
        getSubDomain: getSubDomain
      };
    };
  }
);
