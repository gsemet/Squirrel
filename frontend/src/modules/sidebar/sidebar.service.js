'use strict';

angular.module('squirrel').service('sidebar',

  [

    function() {

      var that = this;
      this.opened = true;
      this.firstTime = true;
      this.NAVIGATE = "navigate";
      this.TOGGLE_GROUP = "toggle_group";

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

      this.isInThisState = function(search, testItem) {
        /*console.log("Searchg if search: " + JSON.stringify(search));
        console.log("is in this item from the collection: " + JSON.stringify(testItem.search));*/
        if (_.isEqual(search, testItem.search)) {
          /*console.log("yes, it's the same (empty)");*/
          return true;
        }
        if (_.isEmpty(search)) {
          return false;
        }
        /* */
        var yes = true;
        _.forEach(search, function(itemSearch, itemSearchkey) {
          /*console.log("comparing itemSearch (key:" + itemSearchkey + "): " +
          JSON.stringify(itemSearchkey) + " " + JSON.stringify(itemSearch)); */
          if (testItem[itemSearchkey] != itemSearch) {
            /*console.log("no, they are not the same");*/
            yes = false;
          }
        });
        /*console.log("returning = " + JSON.stringify(yes));*/
        return yes;
      }
    }

  ]

);
/*
http://stackoverflow.com/questions/14974271/can-you-change-a-path-without-reloading-the-controller-in-angularjs

angular.module('squirrel').run(

  ['$route', '$rootScope', '$location',

    function($route, $rootScope, $location) {
      var original = $location.path;
      $location.path = function(path, reload) {
        if (reload === false) {
          var lastRoute = $route.current;
          var un = $rootScope.$on('$locationChangeSuccess', function() {
            $route.current = lastRoute;
            un();
          });
        }
        return original.apply($location, [path]);
      };
    }
  ]
) * /
*/
