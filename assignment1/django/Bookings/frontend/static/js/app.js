var myApp = angular.module('frontendApp', ['ngResource', 'ui.bootstrap']);

myApp.config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

