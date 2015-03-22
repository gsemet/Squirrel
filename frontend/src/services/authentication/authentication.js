'use strict';

angular.module('squirrel').factory('AuthenticationService',

  ["$http", "$q", "$window", "$rootScope",

    function($http, $q, $window, $rootScope) {
      var userInfo;

      function login(userName, password) {
        var deferred = $q.defer();

        $http.post("http://localhost:8080/api/login", {
          userName: userName,
          password: password
        }).then(function(result) {
          userInfo = {
            accessToken: result.data.access_token,
            userName: result.data.userName
          };
          console.log("login successful for userName = " + JSON.stringify(userName));
          $rootScope.$emit("loginSuccesful", JSON.stringify(userName));
          $window.sessionStorage["userInfo"] = JSON.stringify(userInfo);
          deferred.resolve(userInfo);
        }, function(error) {
          console.log("Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });

        return deferred.promise;
      };

      function getUserInfo() {
        return userInfo;
      };

      return {
        login: login,
        getUserInfo: getUserInfo,
      };
    }
  ]
);
