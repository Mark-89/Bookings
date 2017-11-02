myApp.service('bookingsService', function(bookingsFactory) {
        
    var self = this;
        
    self.getBookings = function getBookings(page) {
        var deferred = bookingsFactory.get({page: page});
        return deferred.$promise
    }             
        
});