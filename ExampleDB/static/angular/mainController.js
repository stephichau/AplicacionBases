(function () {
    'use strict';
    angular.module('exampleDB')
        .controller('mainController', ['$scope', '$rootScope', 'queryService', mainController]);

    function mainController($scope, $rootScope, queryService) {
      var PythonShell = require('python-shell');
      // TODO: Change pythonPath for a virtualenv.
      var pythonOptions = {
        mode: 'text',
        pythonPath: '/path/to/python',
        pythonOptions: ['-u'],
        scriptPath: '/path/to/scripts',
        args: []
      }

      $scope.queryService = queryService;

      function emptyQueryService() {
        queryService.message = "";
        queryService.columns = [];
        queryService.tuples = [];
        queryService.error = false;
      }

      $scope.doQuery = function() {
        emptyQueryService();
        queryService.history.push(queryService.query);
        pythonOptions.args = [queryService.query];
        PythonShell.run('query.py', pythonOptions, function (err, results) {
          if (err) throw err;
          // results is an array consisting of messages collected during execution
          var answer = JSON.parse(results[0]);
          queryService.message = answer.MESSAGE;
          if (answer.STATUS == "ERROR")
          {
            queryService.error = true;
          }
          else {
            queryService.columns = answer.columns;
            queryService.tuples = answer.tuples;
          }
          console.log(queryService);
          $scope.$apply();
        });

      }
    }

})();
