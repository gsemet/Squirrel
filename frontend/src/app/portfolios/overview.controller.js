'use strict';

angular.module("squirrel").controller("PortfoliosOverviewCtrl",

  ["$scope", "$location", "gettextCatalog", "Restangular", "ngTableParams", "$timeout",
  "ModalService", "debug",

    function($scope, $location, gettextCatalog, Restangular, ngTableParams, $timeout,
      ModalService, debug) {

      var basePortfolios = Restangular.all("api/portfolios/p");

      $scope.displayed = [];
      $scope.refresh = function() {
        $scope.displayed = [];
        basePortfolios.getList().then(function(data) {
          $timeout(function() {
            debug.log("PortfoliosOverviewCtrl", "received portfolios data: " + JSON.stringify(data));
            _.forEach(data, function(row) {
              $scope.displayed.push(row);
            });
          }, 300);
        });
      };

      $timeout($scope.refresh, 200);

      var s = $location.search();
      $scope.portfolio_id = s["i"];
      debug.dump("PortfoliosOverviewCtrl", $scope.portfolio_id, "$scope.portfolio_id");
      if ($scope.portfolio_id) {
        debug.info("PortfoliosOverviewCtrl", "We are in portfolio detail, leaving overview controller initialization");
        return;
      }

      $scope.edit = function(row) {
        debug.log("PortfoliosOverviewCtrl", "edit row = " + JSON.stringify(row));
        $location.search("i", row.id);
        $scope.portfolio_id = row.id;
      };

      $scope.createPortfolio = function() {
        // Ex:
        //     http://jsfiddle.net/dwmkerr/8MVLJ/
        ModalService.showModal({
          templateUrl: "app/portfolios/overview.create.template.html",
          controller: "PortfolioOverviewCreateController",
        }).then(function(modal) {
          // The modal object has the element built, if this is a bootstrap modal
          // you can call 'modal' to show it, if it's a custom modal just show or hide
          // it as you need to.
          modal.element.modal();
          modal.close.then(function(data) {
            debug.log("PortfoliosOverviewCtrl", "creating modal result: " + data);
            if (data) {}
          });
        });
      };

      var action = s["a"];
      if (action == "create") {
        debug.log("PortfoliosOverviewCtrl", "a=create, creating portfolios!!");
        $timeout($scope.createPortfolio, 100);
      }
    }
  ]
);

angular.module('squirrel').filter('portfolio_overview_detail_popover', function() {

  return function(row) {
    var output;
    output = "Description: " + row.description + "\n";
    output += "Name: " + row.name + "\n";
    return output;
  }
});
