'use strict';

angular.module('squirrel').service('sidebar',

  [

    function() {

      var that = this;
      this.opened = true;
      this.firstTime = true;

      this.setOpened = function() {
        that.opened = True;
        console.log("setOpened = " + JSON.stringify(that.opened));
      };

      this.toggleOpened = function() {
        that.opened = !that.opened;
        console.log("toggleOpened = " + JSON.stringify(that.opened));
      };

      this.isOpened = function() {
        console.log("isOpened = " + JSON.stringify(that.opened));
        return that.opened;
      };

      this.isFirstTime = function() {
        if (that.firstTime) {
          that.firstTime = false;
          return true;
        }
        return false;
      };
    }

  ]

);
