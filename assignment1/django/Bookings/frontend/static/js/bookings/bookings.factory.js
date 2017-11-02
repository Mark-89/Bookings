myApp.factory('bookingsFactory', function($resource) {
        return $resource("/api/bookings/", 
        {page: "page"});
});