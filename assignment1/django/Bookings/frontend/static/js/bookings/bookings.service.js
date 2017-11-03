myApp.service('bookingsService', function(bookingsFactory) {
        
    var self = this;
        
    self.getBookings = function getBookings(page) {
        var deferred = bookingsFactory.get({page: page});
        return deferred.$promise
    }   
    
    self.searchBookings = function searchBookings(searchObject) {
        var deferred = bookingsFactory.search(searchObject);
        return deferred.$promise
    }             
        
});