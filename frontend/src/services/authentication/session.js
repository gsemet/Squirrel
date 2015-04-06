'use strict';

angular.module('squirrel').service('Session',

  [

    function() {

      this.create = function(sessionId, userId, userName, email, userRole, language) {
        this.id = sessionId;
        this.userId = userId;
        this.userName = userName;
        this.email = email;
        this.userRole = userRole;
        this.language = language;
      };

      this.destroy = function() {
        this.id = null;
        this.userId = null;
        this.userName = null;
        this.email = null;
        this.userRole = null;
        this.language = null;
      };
    }
  ]
);
