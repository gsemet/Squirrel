'use strict';

/*
 * Source
 * https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
 */

angular.module('squirrel').factory('AuthenticationService',

  ["$http", "$q", "$window", "$rootScope", "Session", "AUTH_EVENTS", '$timeout', 'ipCookie', "USER_ROLES",
  "environment", "request",

    function($http, $q, $window, $rootScope, Session, AUTH_EVENTS, $timeout, ipCookie, USER_ROLES,
      environment, request) {

      var authService = {};

      var that = this;

      this.createSession = function(data) {
        Session.create(
          data.id,
          data.userId,
          data.first_name,
          data.last_name,
          data.email,
          data.role,
          data.language
        );
        ipCookie("sessionId", data.id, {
          expires: 15,
          expirationUnit: 'minutes',
        });

        console.log("login successful for email = " + data.email);
        $rootScope.$emit(AUTH_EVENTS.loginSuccess, data.email);
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

        return request.request(environment.getBackendUrl() + "/api/login", {
          /* can be email or email */
          sessionId: sessionId,
        }, "POST").then(function(data) {
          that.createSession(data);
          deferred.resolve(data.email);
        }, function(error) {
          console.log("Restore error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });
      });

      authService.login = function(email, password) {
        return request.request(environment.getBackendUrl() + "/api/login", {
          /* can be email or email */
          email: email,
          password: password
        }, "POST").then(function(data) {
          that.createSession(data);
          deferred.resolve(data.email);
        }, function(error) {
          console.log("Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });
      };

      authService.logout = function() {
        var sessionId = Session.id;
        var email = Session.email;

        console.log("Removing cookie 'sessionId'");
        ipCookie("sessionId", "");
        ipCookie.remove("sessionId");
        Session.destroy();
        $rootScope.$emit(AUTH_EVENTS.logoutSuccess);

        var deferred = $q.defer();
        $http.post(environment.getBackendUrl() + "/api/logout", {
          sessionId: sessionId
        }).then(function(result) {
          console.log("logout successful for email = " + email);
          deferred.resolve(null);
        }, function(error) {
          console.log("Logout error = " + JSON.stringify(error));
          $rootScope.$emit("logoutFailed", error);
          deferred.reject(error);
        });

        return deferred.promise;
      };

      authService.register = function(firstName, lastName, email, password) {
        return request.request(environment.getBackendUrl() + "/api/register", {
          firstName: firstName,
          lastName: lastName,
          email: email,
          password: password
        }, "POST").then(function() {}, function(error) {
          console.log("Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
          deferred.reject(error);
        });
      };

      authService.isAuthenticated = function() {
        return !!Session.userId;
      };

      authService.isAdmin = function() {
        return Session.userRole == USER_ROLES.admin;
      };

      authService.getSessionId = function() {
        return Session.id;
      };

      authService.getEmail = function() {
        return Session.email;
      };

      authService.getFirstName = function() {
        return Session.firstName;
      };

      authService.getLastName = function() {
        return Session.lastName;
      };

      authService.getUserId = function() {
        return Session.userId;
      };

      authService.getUserRole = function() {
        return Session.userRole;
      };

      authService.getUserLanguage = function() {
        return Session.language;
      };

      return authService;
    }
  ]
);
