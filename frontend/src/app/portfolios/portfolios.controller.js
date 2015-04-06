'use strict';

angular.module("squirrel").controller("PortfoliosCtrl",

  ["$scope", "AuthenticationService", "$rootScope", "AUTH_EVENTS", "$location", "gettextCatalog",
    "PortfoliosOverviewCtrl", "PortfoliosSecuritiesCtrl",

    function($scope, AuthenticationService, $rootScope, AUTH_EVENTS, $location, gettextCatalog,
      PortfoliosOverviewCtrl, PortfoliosSecuritiesCtrl) {

      $scope.pages = [
        {
          endpoint: '',
          href: '#/portfolios',
          text: gettextCatalog.getString('Overview'),
          spanicon: 'sub_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/overview.template.html',
          controller: PortfoliosOverviewCtrl
        }, {
          endpoint: 'securities',
          href: '#/portfolios?p=securities',
          text: gettextCatalog.getString('Securities'),
          spanicon: 'sub_icon glyphicon glyphicon-dashboard',
          templateUrl: 'app/portfolios/securities.template.html',
          controller: PortfoliosSecuritiesCtrl
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


      $scope.sidebar_class = "active";
      $scope.toggleSidebar = function() {
        console.log("sidebar toggle");
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
        console.log("activeIfCurrentPageIs");
        console.log("current_page = " + JSON.stringify(current_page));
        console.log("page = " + JSON.stringify(page));
        if (current_page == page) {
          return "active";
        }
        return "";
      };
    }
  ]
);
