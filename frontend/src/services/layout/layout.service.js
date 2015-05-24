'use strict';

angular.module('squirrel').service('layout',

  ["$location", "debug",

    function($location, debug) {

      var that = this;

      this.showFooter = function() {
        debug.dump("layout", $location.path(), "$location.path()")
        if ($location.path() === "/") {
          debug.log("layout", "display footer on homepage!")
          return true;
        }
        var currentRoute = $location.path().substring(1) || '/';
        var hide_in_pages = [
          "/admin",
          "/register",
          "/login",
        ];
        var page = $location.path();
        /*debug.log("layout", "page = " + JSON.stringify(page));*/
        var v = !_.contains(hide_in_pages, page);
        debug.log("layout", "display footer: " + JSON.stringify(v));
        return v;
      };

      this.isFullPage = function() {
        if ($location.path() === "/" && page === '') {
          debug.log("layout", "display footer on homepage!")
          return false;
        }
        var currentRoute = $location.path().substring(1) || '/';
        var hide_in_pages = [
          "/register",
          "/login",
        ];
        var page = $location.path();
        /*debug.log("layout", "page = " + JSON.stringify(page));*/
        var v = _.contains(hide_in_pages, page);
        /*debug.log("layout", "display footer: " + JSON.stringify(v));*/
        return v;
      };
    }
  ]
);
