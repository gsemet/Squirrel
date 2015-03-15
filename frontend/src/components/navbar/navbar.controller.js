'use strict';

angular.module('squirrel')
  .controller('NavbarCtrl', ["$scope", "$location", function($scope, $location) {
    $scope.date = new Date();

    $scope.navLinks = [
      {
        endpoint: 'screeners',
        linktext: 'Stock Screeners'
      }, {
        endpoint: 'my-portfolios',
        linktext: 'My Portfolios'
      }, {
        endpoint: 'doc',
        linktext: 'Documentation'
      }
    ];

    $scope.navClass = function(page) {
      console.log("location: " + $location.path() + ", page: " + page);
      if ($location.path() === "/" && page === '') {
        console.log("returning active!")
        return "active";
      }
      var currentRoute = $location.path().substring(1) || '/';
      return page === currentRoute ? 'active' : '';
    };
  }]);
