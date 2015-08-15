'use strict';

/*
 * Source
 * https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
 */

angular.module('squirrel').factory('AuthenticationService',

  ["$http", "$q", "$window", "$rootScope", "Session", "AUTH_EVENTS", '$timeout', 'ipCookie',
  "USER_ROLES", "environment", "request", "debug",

    function($http, $q, $window, $rootScope, Session, AUTH_EVENTS, $timeout, ipCookie, USER_ROLES,
      environment, request, debug) {

      var authService = {};
      var that = this;

      this.createSession = function(data) {
        Session.create(
          data
        );
        ipCookie("sessionId", data.session_id, {
          expires: 15,
          expirationUnit: 'minutes',
        });

        debug.dump("authentication", data.email, "login successful for email");
        $rootScope.$emit(AUTH_EVENTS.loginSuccess, data.email);
        /*$window.sessionStorage["userInfo"] = JSON.stringify(userInfo);*/

      };

      $timeout(function() {
        debug.debug("authentication", "Trying to restore session");
        var sessionId = ipCookie('sessionId');
        if (!sessionId) {
          return;
        }
        debug.dump("authentication", JSON.stringify(sessionId), "Restoring sessionId");

        return request.request("/api/login", {
          /* can be email or email */
          sessionId: sessionId,
        }, "POST").then(function(data) {
          that.createSession(data);
        }, function(error) {
          debug.dump("authentication", JSON.stringify(error), "Restore error");
          $rootScope.$emit("loginFailed", error);
        });
      });

      authService.login = function(email, password) {
        return request.request("/api/login", {
          /* can be email or email */
          email: email,
          password: password
        }, "POST").then(function(data) {
          that.createSession(data);
          debug.dump("authentication", JSON.stringify(data), "login success, got data");
        }, function(error) {
          debug.dump("authentication", JSON.stringify(error), "Login error");
          $rootScope.$emit("loginFailed", error);
        });
      };

      authService.logout = function() {
        var sessionId = Session.id;
        var email = Session.email;

        debug.debug("authentication", "Removing cookie 'sessionId'");
        ipCookie("sessionId", "");
        ipCookie.remove("sessionId");
        Session.destroy();
        $rootScope.$emit(AUTH_EVENTS.logoutSuccess);

        $http.post("/api/logout", {
          sessionId: sessionId
        }).then(function(result) {
          debug.dump("authentication", email, "logout successful for email ");
        }, function(error) {
          debug.dump("authentication", JSON.stringify(error), "Logout error");
          $rootScope.$emit("logoutFailed", error);
        });
      };

      authService.register = function(firstName, lastName, email, password) {
        return request.request("/api/register", {
          firstName: firstName,
          lastName: lastName,
          email: email,
          password: password
        }, "POST").then(function() {}, function(error) {
          debug.debug("authentication", "Login error = " + JSON.stringify(error));
          $rootScope.$emit("loginFailed", error);
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

      authService.getFeatures = function() {
        return Session.features;
      };

      return authService;
    }
  ]
);
