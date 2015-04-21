'use strict';

angular.module('squirrel').service('Session',

  [

    function() {

      this.create = function(sessionId, userId, firstName, lastName, email, userRole, language) {
        this.id = sessionId;
        this.userId = userId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.userRole = userRole;
        this.language = language;
      };

      this.destroy = function() {
        this.id = null;
        this.userId = null;
        this.firstName = null;
        this.lastName = null;
        this.email = null;
        this.userRole = null;
        this.language = null;
      };
    }
  ]
);
