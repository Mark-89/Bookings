var myApp = angular.module('frontendApp', ['ngResource']);

myApp.config(function($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

myApp.controller('MainCtrl', function($scope, bookingsService, bookingsFactory) {
      
    var self = this;    
    self.bookings = [];
    
 
    function getBookings() {
        bookingsService.getBookings()
        .then(function (serverData) {
                self.bookings = serverData.results;
      });
       
    }      
  
      
    function activate() {
       getBookings()
      }
      
      activate();
});
