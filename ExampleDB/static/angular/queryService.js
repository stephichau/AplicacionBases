(function () {
    'use strict';
    angular.module('exampleDB')
        .service('queryService', queryService);

    function queryService() {
      var query = "";
      var history = [];
      var message = "";
      var columns = [];
      var tuples = [];
      var error = false;

      return {
        query: query,
        history: history,
        message: message,
        columns: columns,
        tuples: tuples,
        error: error
      };
    }



})();
