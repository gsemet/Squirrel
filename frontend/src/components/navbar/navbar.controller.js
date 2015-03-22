'use strict';

angular.module('squirrel').controller('NavbarCtrl',

  ["$scope", "$location", "$rootScope", "AuthenticationService",

    function($scope, $location, $rootScope, AuthenticationService) {

      $scope.date = new Date();
      $scope.login_username = "";

      $scope.navLinks = [
        {
          endpoint: 'screeners',
          linktext: 'Stock Screeners'
        }, {
          endpoint: 'my-portfolios',
          linktext: 'My Portfolios'
        }
      ];

      $scope.loginLinks = [
        {
          endpoint: 'login',
          linktext: 'Login'
        }, {
          endpoint: 'register',
          linktext: 'Register'
        }
      ];

      $rootScope.$on("loginSuccesful", function(event, userName) {
        console.log("navbar on loginSuccesful1:" + userName);
        $scope.login_username = userName;
      });

      $rootScope.$on("logoutSuccesful", function(event) {
        console.log("navbar on logout");
        $scope.login_username = "";
      });

      $rootScope.$on("loginError", function(event, error) {
        console.log("navbar on loginError:" + error);
        $scope.login_username = "";
      });

      $scope.logout = function() {
        console.log("log out !!!");
        AuthenticationService.logout();
      }

      $scope.navClass = function(page) {
        /*console.log("location: " + $location.path() + ", page: " + page);*/
        if ($location.path() === "/" && page === '') {
          /*console.log("returning active!")*/
          return "active";
        }
        var currentRoute = $location.path().substring(1) || '/';
        return page === currentRoute ? 'active' : '';
      };
    }
  ]
);
