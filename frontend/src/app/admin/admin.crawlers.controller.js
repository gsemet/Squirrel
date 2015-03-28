'use strict';

angular.module('squirrel').controller('AdminCrawlersCtrl',

  ['$scope', "_", "$q", "$http", "toaster",

    function($scope, _, $q, $http, toaster) {

      $scope.crawlers = null;
      toaster.pop('success', "title", "text");
      $scope.getAllCrawlers = function() {
        var deferred = $q.defer();

        $http.get("http://localhost:8080/api/crawlers").then(function(result) {
          var all_crawlers = [];
          _.forEach(result.data, function(item) {
            toaster.pop('success', 'Crawlers found', JSON.stringify(item));
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
    }
  ]
);
