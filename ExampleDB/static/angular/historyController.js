(function () {
    'use strict';
    angular.module('exampleDB')
        .controller('historyController', ['$scope', '$rootScope', 'queryService', historyController]);

    function historyController($scope, $rootScope, queryService) {
      $scope.queryService = queryService;

      $scope.useQuery = function(id) {
        queryService.query = queryService.history[id];
      }
    }

})();
