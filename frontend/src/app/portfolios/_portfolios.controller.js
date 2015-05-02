'use strict';

angular.module("squirrel").controller("PortfoliosCtrl",

  ["$scope", "AuthenticationService", "$rootScope", "AUTH_EVENTS", "$location", "gettextCatalog",
  'Restangular', '$timeout', "debug",

    function($scope, AuthenticationService, $rootScope, AUTH_EVENTS, $location, gettextCatalog,
      Restangular, $timeout, debug) {

      $scope.is_admin = AuthenticationService.isAdmin();
      $scope.endpoint = "#/portfolios";

      var page_key = 'p';

      var s = $location.search()
      if (!s[page_key]) {
        $location.search("p", "summary");
      }

      $scope.portfolioIndex = 0;
      $scope.menuItems = [
        {
          search: {
            'p': 'summary'
          },
          name: gettextCatalog.getString('Summary'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/summary.template.html',
        }, {
          search: {
            'p': 'securities'
          },
          name: gettextCatalog.getString('Securities'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/securities.template.html',
        }, {
          search: {
            'p': 'cash'
          },
          name: gettextCatalog.getString('Cash'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/cash.template.html',
        }, {
          search: {
            'p': 'allocations'
          },
          name: gettextCatalog.getString('Allocations'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/allocations.template.html',
        }, {
          search: {
            'p': 'covers'
          },
          name: gettextCatalog.getString('Covers'),
          icon: 'glyphicon glyphicon-book',
          templateUrl: 'app/portfolios/covers.template.html',
        }, {
          search: {
            'p': 'timeline', // == move history
          },
          name: gettextCatalog.getString('Timeline'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/timeline.template.html',
        }, {
          search: {
            'p': 'status_report'
          },
          name: gettextCatalog.getString('Status Report'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/status_report.template.html',
        }, {
          search: {
            'p': 'reporting'
          },
          name: gettextCatalog.getString('Reporting'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/reporting.template.html',
        }, {
          search: {
            'p': 'annual_reports'
          },
          name: gettextCatalog.getString('Annual Reports'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/annual_reports.template.html',
        }, {
          search: {
            'p': 'taxation'
          },
          name: gettextCatalog.getString('Taxation'),
          icon: 'glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/taxation.template.html',
        }
      ];

      $scope.is_logged = AuthenticationService.isAuthenticated();
      debug.log("PortfoliosCtrl", "my portofolio is_logged = " + JSON.stringify($scope.is_logged));

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      var basePortfolios = Restangular.all("api/portfolios/p");

      $scope.portfolios = [];
      $scope.refresh = function() {
        $scope.portfolios = [];
        basePortfolios.getList().then(function(data) {
          $timeout(function() {
            console.log("received portfolios data for sidebar: " + JSON.stringify(data));
            $scope.menuItems[$scope.portfolioIndex]['children'] = []
            _.forEach(data, function(row) {
              $scope.portfolios.push(row);
              $scope.menuItems[$scope.portfolioIndex]['children'].push({
                search: {
                  'p': 'overview',
                  'i': row.id,
                },
                name: row.name,
                icon: 'glyphicon glyphicon-dashboard',
                templateUrl: 'app/portfolios/overview.template.html',
              });
            });
          }, 500);
        });
      };
      $timeout($scope.refresh, 500);

      $scope.sidebar_class = "active";
      $scope.toggleSidebar = function() {
        if ($scope.sidebar_class == "active") {
          $scope.sidebar_class = "";
        } else {
          $scope.sidebar_class = "active";
        }
      };

      $scope.currentPage = function(page) {
        var s = $location.search();
        if (_.isEmpty(s['p'])) {
          return "";
        }
        return s['p'];
      };

      $scope.activeIfCurrentPageIs = function(page) {
        var s = $location.search();
        var current_page;
        if (_.isEmpty(s['p'])) {
          current_page = "";
        } else {
          current_page = s['p'];
        }
        if (current_page == page) {
          return "active";
        }
        return "";
      };

      $scope.activeIfCurrentPortfolioIdIs = function(portfolioId) {
        var s = $location.search();
        if (_.isEmpty(s['i'])) {
          return "";
        } else {
          var current_portfolio_id = s['i'];
          debug.dump("PortfoliosCtrl", current_portfolio_id, "current_portfolio_id");
          debug.dump("PortfoliosCtrl", portfolioId, "portfolioId");
          if (+current_portfolio_id == +portfolioId) {
            return "active";
          }
          return "";
        }
      };

      /*
      $scope.loadController = function(controller) {
        debug.dump("controller = " + JSON.stringify(controller));
        var c = $controller(controller, {
          $scope: $scope
        });
        debug.dump("$controller = " + c);
        return c;
      };*/
        }
        ]
);
