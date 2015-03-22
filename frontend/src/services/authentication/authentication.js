'use strict';

/*
 * Source
 * https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
 */

angular.module('squirrel').factory('AuthenticationService',

  ["$http", "$q", "$window", "$rootScope", "Session", "AUTH_EVENTS", '$timeout', 'ipCookie',

    function($http, $q, $window, $rootScope, Session, AUTH_EVENTS, $timeout, ipCookie) {

      var authService = {};

      var that = this;

      this.createSession = function(data) {
        Session.create(
          data.id,
          data.userId,
          data.userName,
          data.email,
          data.role
        );
        ipCookie("sessionId", data.id, {
          expires: 15,
          expirationUnit: 'minutes',
        });

        console.log("login successful for userName = " + data.userName);
        $rootScope.$emit(AUTH_EVENTS.loginSuccess, data.userName);
        /*$window.sessionStorage["userInfo"] = JSON.stringify(userInfo);*/

      };

      $timeout(function() {
        console.log("Trying to restore session");
        var sessionId = ipCookie('sessionId');
        if (!sessionId) {
          return;
        }
        console.log("Restoring sessionId = " + JSON.stringify(sessionId));

        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/profile", {
          /* can be username or email */
          sessionId: sessionId,
        }).then(function(result) {
          that.createSession(result.data);
          deferred.resolve(result.data.userName);
        }, function(error) {
          console.log("Restore error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });
        return deferred.promise;
      });

      authService.login = function(userName, password) {
        var deferred = $q.defer();

        $http.post("http://localhost:8080/api/login", {
          /* can be username or email */
          userName: userName,
          password: password
        }).then(function(result) {
          that.createSession(result.data);
          deferred.resolve(result.data.userName);
        }, function(error) {
          console.log("Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });

        return deferred.promise;
      };

      authService.logout = function() {
        var sessionId = Session.id;
        var userName = Session.userName;

        console.log("Removing cookie 'sessionId'");
        ipCookie("sessionId", "");
        ipCookie.remove("sessionId");
        Session.destroy();
        $rootScope.$emit(AUTH_EVENTS.logoutSuccess);

        var deferred = $q.defer();
        $http.post("http://localhost:8080/api/logout", {
          sessionId: sessionId
        }).then(function(result) {
          console.log("logout successful for userName = " + userName);
          deferred.resolve(null);
        }, function(error) {
          console.log("Logout error = " + JSON.stringify(error));
          $rootScope.$emit("logoutFailed", error);
          deferred.reject(error);
        });

        return deferred.promise;
      };

      authService.register = function(userName, email, password) {
        var deferred = $q.defer();

        $http.post("http://localhost:8080/api/register", {
          userName: userName,
          email: email,
          password: password
        }).then(function(result) {
          deferred.resolve(userName);
        }, function(error) {
          console.log("Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });

        return deferred.promise;
      };

      authService.isAuthenticated = function() {
        return !!Session.userId;
      };

      authService.getUserName = function() {
        return Session.userName;
      };

      authService.getSessionId = function() {
        return Session.id;
      };

      authService.getEmail = function() {
        return Session.email;
      };

      authService.getUserId = function() {
        return Session.userId;
      };

      authService.getUserRole = function() {
        return Session.userRole;
      };

      return authService;
    }
  ]
);
