'use strict';

angular.module('squirrel').controller('AdminCrawlersCtrl',

  ['$scope', "_", "$q", "$http", "toastr",

    function($scope, _, $q, $http, toastr) {

      $scope.crawlers = null;
      $scope.getAllCrawlers = function() {
        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers").then(function(result) {
          var all_crawlers = [];
          console.log("Refreshing crawlers");
          _.forEach(result.data, function(item) {
            toastr.success('Crawlers found : ' + JSON.stringify(item), 'Crawlers found');
            all_crawlers.push(item);
          });
          $scope.crawlers = all_crawlers;
          deferred.resolve(result.data);
        }, function(error) {
          console.log("Get all crawlers error = " + JSON.stringify(error));
          deferred.reject(error);
        });
        return deferred.promise;
      };
      // refreshing all crawlers immediately after the creation of the
      setTimeout(function() {
        $scope.getAllCrawlers();
      }, 0);

      $scope.crawlerStart = function(name) {
        toastr.success('Starting crawler ' + name, 'Starting');
      }
      $scope.crawlerStop = function(name) {
        toastr.success('Stopping crawler ' + name, 'Stopping');
      }
      $scope.crawlerShowLogs = function(name) {
        toastr.success('Showing crawler logs: ' + name, 'Showing logs');
      }
    }
  ]
);
