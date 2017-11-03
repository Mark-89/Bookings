myApp.factory('bookingsFactory', function($resource) {
        return $resource("/api/bookings/", 
        {},
        {
            'search': {
                method: "GET",
                isArray: false,               
                url: "/api/bookings/search/"
            }
        });
})