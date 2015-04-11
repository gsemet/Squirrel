'use strict';

angular.module("squirrel").controller("PortfoliosCtrl",

  ["$scope", "AuthenticationService", "$rootScope", "AUTH_EVENTS", "$location", "gettextCatalog",
  'Restangular', '$timeout',

    function($scope, AuthenticationService, $rootScope, AUTH_EVENTS, $location, gettextCatalog,
      Restangular, $timeout) {

      $scope.pages = [
        {
          endpoint: '',
          href: '#/portfolios',
          text: gettextCatalog.getString('Overview'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/overview.template.html',
          /*controller: "PortfoliosOverviewCtrl"  => hard to make it work */
        }, {
          endpoint: 'securities',
          href: '#/portfolios?p=securities',
          text: gettextCatalog.getString('Securities'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/securities.template.html',
          /*controller: "PortfoliosSecuritiesCtrl"*/
        }, {
          endpoint: 'allocations',
          href: '#/portfolios?p=allocations',
          text: gettextCatalog.getString('Allocations'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/allocations.template.html',
          /*controller: "PortfoliosSecuritiesCtrl"*/
        }, {
          endpoint: 'timeline', // == move history
          href: '#/portfolios?p=timeline',
          text: gettextCatalog.getString('Timeline'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/timeline.template.html',
        }, {
          endpoint: 'status_report',
          href: '#/portfolios?p=status_report',
          text: gettextCatalog.getString('Status Report'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/status_report.template.html',
        }, {
          endpoint: 'reporting',
          href: '#/portfolios?p=reporting',
          text: gettextCatalog.getString('Reporting'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/reporting.template.html',
        }, {
          endpoint: 'annual_reports',
          href: '#/portfolios?p=annual_reports',
          text: gettextCatalog.getString('Annual Reports'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/annual_reports.template.html',
        }, {
          endpoint: 'taxation',
          href: '#/portfolios?p=taxation',
          text: gettextCatalog.getString('Taxation'),
          spanicon: 'navbar_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/taxation.template.html',
        }
      ];

      $scope.is_logged = AuthenticationService.isAuthenticated();
      console.log("my portofolio is_logged = " + JSON.stringify($scope.is_logged));

      $rootScope.$on(AUTH_EVENTS.loginSuccess, function(event, userName) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.logoutSuccess, function(event) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      $rootScope.$on(AUTH_EVENTS.loginFailed, function(event, error) {
        $scope.is_logged = AuthenticationService.isAuthenticated();
      });

      var basePortfolios = Restangular.all("api/portfolios");

      $scope.portfolios = [];
      $scope.refresh = function() {
        $scope.portfolios = [];
        basePortfolios.getList().then(function(data) {
          $timeout(function() {
            console.log("received portfolios data for sidebar: " + JSON.stringify(data));
            _.forEach(data, function(row) {
              $scope.portfolios.push(row);
            });
          }, 100);
        });
      };
      $timeout($scope.refresh, 100);

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
          console.log("current_portfolio_id = " + JSON.stringify(+current_portfolio_id));
          console.log("portfolioId = " + JSON.stringify(+portfolioId));
          if (+current_portfolio_id == +portfolioId) {
            return "active";
          }
          return "";
        }
      };

      /*
      $scope.loadController = function(controller) {
        console.log("controller = " + JSON.stringify(controller));
        var c = $controller(controller, {
          $scope: $scope
        });
        console.log("$controller = " + c);
        return c;
      };*/
    }
  ]
);
