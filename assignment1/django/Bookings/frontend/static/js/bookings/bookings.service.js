myApp.service('bookingsService', function(bookingsFactory) {
        
    var self = this;
        
    self.getBookings = function getBookings() {
        var deferred = bookingsFactory.get();
        return deferred.$promise
    }             
        
});