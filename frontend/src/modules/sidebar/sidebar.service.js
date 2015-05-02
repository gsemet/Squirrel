'use strict';

angular.module('squirrel').service('sidebar',

  ["debug",

    function(debug) {

      var that = this;
      this.opened = true;
      this.firstTime = true;
      this.NAVIGATE = "sidebar-navigate";
      this.DISPLAY_PAGE = "sidebar-display";
      this.TOGGLE_GROUP = "sidebar-toggle-group";

      this.setOpened = function() {
        that.opened = True;
        /*        debug.dump("SidebarService", that.opened, "setOpened");*/
      };

      this.toggleOpened = function() {
        that.opened = !that.opened;
        /*debug.dump("SidebarService", that.opened, "toggleOpened");*/
      };

      this.isOpened = function() {
        /*debug.dump("SidebarService", that.opened, "isOpened");*/
        return that.opened;
      };

      this.isFirstTime = function() {
        if (that.firstTime) {
          that.firstTime = false;
          return true;
        }
        return false;
      };

      this.isInThisState = function(search, itemCollection) {
        /*debug.dump("SidebarService", search, "Searching if 'search'");*/
        /*debug.dump("SidebarService", itemCollection.search, "is in this item from the collection: ");*/
        if (_.isEqual(search, itemCollection.search)) {
          /*debug.debug("SidebarService", "yes, it's the same (empty)");*/
          return true;
        }
        if (_.isEmpty(search)) {
          return false;
        }
        /* */
        var found = false;
        _.forEach(search, function(itemSearch, itemSearchkey) {
          /*debug.dump("SidebarService", itemCollection.search, "itemCollection.search")*/
          /*debug.debug("SidebarService", "comparing itemSearch (key: '" + itemSearchkey + "'): " +
            JSON.stringify(itemCollection.search[itemSearchkey]) + " with " + JSON.stringify(itemSearch));*/
          if (!itemCollection.search[itemSearchkey] || itemCollection.search[itemSearchkey] != itemSearch) {
            /*debug.debug("SidebarService", "no, they are not the same");*/
          } else {
            /*debug.debug("SidebarService", "Yes they are the same!");*/
            found = true;
            return; /* like a break */
          }
        });
        /*debug.debug("SidebarService", "returning " + found);*/
        return found;
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
