'use strict';

angular.module('squirrel').provider('environment',

  function() {

    // Example:
    // [{
    //   environment: 'local',
    //   appUseSSL: false,
    //   appUrl: 'localhost',
    //   appPort: '9000', // only if using a non-standard port (80 or 443)
    //   serviceUseSSL: false,
    //   serviceUrl: 'myApp-dev.servercom' // optional: if different from appUrl,
    //   servicePort: '8080' // only if using a non-standard port (80 or 443)
    // },
    // {
    //   environment: 'dev',
    //   appUrl: 'myApp-dev.servercom'
    // },
    // {
    //   environment: 'preview',
    //   appUrl: 'myApp-pre.servercom'
    // },
    // {
    //   environment: 'prod',
    //   appUrl: 'subdomain.servercom/myAppVirtualDirectory'
    // }];

    // DEFAULT
    this.list = [{
      environment: 'local',
      appUrl: '127.0.0.1',
      appPort: '9000'
    }];

    this.setList = function(list) {
      this.list = list;
    };


    this.$get = function($location) {
      var list = this.list;
      var host = $location.host();
      var env = {};

      var currentEnvironment = function() {

        host = host.toLowerCase();

        if (_.isArray(list) && list.length > 0) {
          env = _.find(list, function(environment) {
            var lowercaseUrl = environment.appUrl.toLowerCase();
            return (lowercaseUrl == host);
          });

          if (!env) {
            //Environment not found fall back to a default.
            env = list[0];
          }
        }

        return env;
      };

      var getEnvironment = function() {
        var enviro = currentEnvironment();
        console.log('enviro: ' + enviro);
        return (enviro) ? enviro.environment : 'local';
      };

      var getAppUrl = function() {
        var env = currentEnvironment();
        var currentSSL = (env.appUseSSL) ? 'https://' : 'http://';
        var currentAppUrl = (env.appUrl) ? env.appUrl : list.appUrl;
        var currentAppPort = (env.appPort) ? ':' + env.appPort : '';

        return currentSSL + currentAppUrl + currentAppPort;
      };

      var getServiceUrl = function() {
        var env = currentEnvironment();
        var currentSSL = (env.serviceUseSSL) ? 'https://' : 'http://';
        var currentServiceUrl = (env.serviceUrl) ? env.serviceUrl : env.appUrl;
        var currentServicePort = (env.servicePort) ? ':' + env.servicePort : '';

        currentServicePort = (!env.servicePort && !env.serviceUrl) ? ':' + env.appPort : currentServicePort;

        return currentSSL + currentServiceUrl + currentServicePort;
      };

      return {
        getEnvironment: getEnvironment,
        getAppUrl: getAppUrl,
        getServiceUrl: getServiceUrl
      };
    };
  }
);
