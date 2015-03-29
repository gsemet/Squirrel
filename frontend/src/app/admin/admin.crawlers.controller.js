'use strict';

angular.module('squirrel').controller('AdminCrawlersCtrl',

  ['$scope', "_", "$q", "$http", "toastr", "$interval",

    function($scope, _, $q, $http, toastr, $interval) {

      $scope.crawlers = null;

      //////////////////////////////////////////////////////////////////////////////////////////////
      /// Refresh Crawlers
      $scope.getAllCrawlers = function() {
        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers").then(function(result) {
          var all_crawlers = [];
          console.log("Refreshing crawlers");
          _.forEach(result.data, function(item) {
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

      $scope.crawlerStart = function(name) {
        toastr.success('Starting crawler ' + name, 'Starting');
        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers/" + name + "?action=start").then(function(result) {
          console.log("request sent: start" + result.data);

          deferred.resolve(result.data);
        }, function(error) {
          console.log("error = " + JSON.stringify(error));
          toastr.failure('Error when starting ' + name, 'Error');
          deferred.reject(error);
        });
        return deferred.promise;
      };
      $scope.crawlerStop = function(name) {
        toastr.success('Stopping crawler ' + name, 'Stopping');
        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers/" + name + "?action=stop").then(function(result) {
          console.log("request sent: stop" + result.data);

          deferred.resolve(result.data);
        }, function(error) {
          console.log("error = " + JSON.stringify(error));
          toastr.failure('Error when stopping ' + name, 'Error');
          deferred.reject(error);
        });
        return deferred.promise;
      };
      $scope.crawlerShowLogs = function(name) {
        toastr.success('Showing crawler logs: ' + name, 'Showing logs');

        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers/" + name + "?action=progress").then(function(result) {
          console.log("request sent: progress" + result.name);

          deferred.resolve(result.data);
        }, function(error) {
          console.log("error = " + JSON.stringify(error));
          toastr.failure('Error when shwowing log of ' + name, 'Error');
          deferred.reject(error);
        });
        return deferred.promise;
      };

      //////////////////////////////////////////////////////////////////////////////////////////////
      /// Refresh on interval
      var stop;
      $scope.refresh = function() {
        if (angular.isDefined(stop)) return;

        stop = $interval(function() {
          console.log("refresh!");
          $scope.getAllCrawlers();
        }, 1000);
      };
      $scope.refresh();

      $scope.stopRefresh = function() {
        if (angular.isDefined(stop)) {
          $interval.cancel(stop);
          stop = undefined;
        }
      };

      $scope.$on('$destroy', function() {
        // Make sure that the interval is destroyed too
        $scope.stopRefresh();
      });
    }
  ]
);
