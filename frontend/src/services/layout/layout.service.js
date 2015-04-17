'use strict';

angular.module('squirrel').service('layout',

  ["$location",

    function($location) {

      var that = this;

      this.showFooter = function() {
        if ($location.path() === "/" && page === '') {
          console.log("display footer on homepage!")
          return true;
        }
        var currentRoute = $location.path().substring(1) || '/';
        var hide_in_pages = [
          "/admin",
          "/register",
          "/login",
        ];
        var page = $location.path();
        /*console.log("page = " + JSON.stringify(page));*/
        var v = !_.contains(hide_in_pages, page);
        /*console.log("display footer: " + JSON.stringify(v));*/
        return v;
      };

      this.isFullPage = function() {
        if ($location.path() === "/" && page === '') {
          console.log("display footer on homepage!")
          return false;
        }
        var currentRoute = $location.path().substring(1) || '/';
        var hide_in_pages = [
          "/register",
          "/login",
        ];
        var page = $location.path();
        /*console.log("page = " + JSON.stringify(page));*/
        var v = _.contains(hide_in_pages, page);
        /*console.log("display footer: " + JSON.stringify(v));*/
        return v;
      };
    }
  ]
);
