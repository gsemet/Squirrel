'use strict';

angular.module("squirrel").controller("PortfolioCreateController",

  ["$scope", "$location", "gettextCatalog", "Restangular", "LocationWatcherService", "request",
  "$sce", "debug",

    function($scope, $location, gettextCatalog, Restangular, LocationWatcherService, request,
      $sce, debug) {

      $scope.portfolioTypes = {};
      $scope.currentType = null;
      $location.search("a", "create");

      $scope.refresh = function() {
        debug.dump("PortfolioCreateController", $scope.currentType, "$scope.currentType");
        if ($scope.currentType) {
          _.forEach($scope.types, function(item) {
            debug.dump("PortfolioCreateController", item, "item");
            debug.dump("PortfolioCreateController", item[0], "item[0]");
            debug.dump("PortfolioCreateController", item[1], "item[1]");
            if (item[1] == $scope.currentType) {
              $scope.portfolioTypes = {
                selected: item
              };
            }
          });
        }
      };

      $scope.getPortfolioTypes = function() {
        request.request("api/portfolios/types").then(function(data) {
          debug.dump("PortfolioCreateController", data, "received portfolios types");
          $scope.portfolioTypes = data;
          /*$scope.portfolioTypes = _.filter(data, function(item) {
            debug.dump("PortfolioCreateController", item, "before");
            var v = [he.decode(item[0]), he.decode(item[1])];
            debug.dump("PortfolioCreateController", v, "after");
            return v;
          });*/
          $scope.refresh();
          $scope.createPortfolio.$setPristine();
          $scope.createPortfolio.portfolioType.$setPristine();
        });
      };
      $scope.getPortfolioTypes();

      $scope.groupPerAccountTypes = function(item) {
        return item[0];
      };

      /*
      $scope.setupWatchers = function($scope, scopeVarName, nameKey) {
        $scope.$watch(function() {
          return $location.search();
        }, function() {
          $scope[scopeVarName] = $location.search()[nameKey] || "";
        });
        $scope.$watch(scopeVarName, function(portfolioName) {
          $location.search(nameKey, portfolioName);
        });
      };
      */
      LocationWatcherService.setupWatchers($scope, "portfolioName", "n");
      LocationWatcherService.setupWatchers($scope, "portfolioDescription", "d");
      LocationWatcherService.setupWatchers($scope, "portfolioTypes.selected[1]", "t");
    }
  ]
);

angular.module('squirrel').service('PortfolioCreateService',

  ["debug", "Restangular", "ModalService",

    function(debug, Restangular, ModalService) {

      this.createPortfolio = function(search, itemCollection) {

        // Ex:
        //     http://jsfiddle.net/dwmkerr/8MVLJ/
        ModalService.showModal({
          templateUrl: "app/portfolios/create.template.html",
          controller: "PortfolioCreateController",
        }).then(function(modal) {
          // The modal object has the element built, if this is a bootstrap modal
          // you can call 'modal' to show it, if it's a custom modal just show or hide
          // it as you need to.
          modal.element.modal();
          modal.close.then(function(data) {
            debug.log("PortfolioCreateService", "creating modal result: " + data);
            if (data) {}
          });
        });

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
