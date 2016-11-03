'use strict';

(function () {
  var app = angular.module('exampleDB', ['ngRoute','ngMaterial']).config(['$routeProvider', appRoutes]);

  function appRoutes($routeProvider) {
    $routeProvider.when('/', {
      templateUrl: 'static/templates/main.html' ,
      controller: 'mainController',
      controllerAs: 'mainCtrl'
    }).when('/history', {
      templateUrl: 'static/templates/history.html' ,
      controller: 'historyController',
      controllerAs: 'historyCtrl'
    }).when('/about', {
      templateUrl: 'static/templates/about.html' ,
      controller: 'aboutController',
      controllerAs: 'aboutCtrl'
    });
    $routeProvider.otherwise({ redirectTo: '/' });
  }
})();
