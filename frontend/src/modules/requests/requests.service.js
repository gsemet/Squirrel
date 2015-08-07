'use strict';

angular.module('squirrel').factory('request',

  ['$http', '$q', "debug",

    function($http, $q, debug) {

      // URL required; rest are optional
      var request = function(url, params, verb, data, cache) {
        var deferred = $q.defer();
        debug.debug("requests", "Request: url = " + ((verb) ? verb : 'GET') + JSON.stringify(url));
        $http({
          method: (verb) ? verb : 'GET',
          url: url,
          data: data,
          params: params,
          withCredentials: true,
          cache: (cache),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
        }).success(function(response) {
          deferred.resolve(response.value || response.data || response);
        }).error(function(response) {
          debug.error("navbar", JSON.stringify(response));
          deferred.reject(response);
        });

        return deferred.promise;
      };

      // requestSettings: from $http documentation
      // method: string
      // url: string
      // params: object
      // data: string/object
      // headers: object
      // xsrfHeaderName: string
      // xsrfCookieName: string
      // transformRequest
      // transformResponse
      // cache: boolean or Cache
      // timeout: number or Promise
      // withCredentials: boolean
      // responseType: string
      var requestRaw = function(requestSettings) {
        var deferred = $q.defer();
        $http(requestSettings).success(function(data, status, headers, config) {
          var response = {
            data: data,
            status: status,
            headers: headers(),
            config: config
          };
          deferred.resolve(response);
        }).error(function(data, status, headers, config) {
          var response = {
            data: data,
            status: status,
            headers: headers,
            config: config
          };
          deferred.reject(response);
        });
        return deferred.promise;
      };

      return {
        request: request,
        requestRaw: requestRaw
      }
    }
  ]
);
