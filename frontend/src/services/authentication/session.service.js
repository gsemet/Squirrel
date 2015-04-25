'use strict';

angular.module('squirrel').service('Session',

  ["USER_ROLES",

    function(USER_ROLES) {

      var that = this;

      this.create = function(data) {
        this.id = data.session_id;
        this.userId = data.user_id;
        this.firstName = data.first_name;
        this.lastName = data.last_name;
        this.email = data.email;
        this.userRole = data.role;
        this.language = data.language;
        this.features = data.features;
        console.log("Creating session for user = " + JSON.stringify(this.firstName) + ", email " +
          JSON.stringify(this.email), ", role: " + JSON.stringify(this.userRole));
      };

      this.destroy = function() {
        this.id = null;
        this.userId = null;
        this.firstName = null;
        this.lastName = null;
        this.email = null;
        this.userRole = null;
        this.language = null;
        this.features = null;
      };

      this.isAuthenticated = function() {
        return !!this.userId;
      };

      this.isAdmin = function() {
        return this.userRole == USER_ROLES.admin;
      };
    }
  ]
);
