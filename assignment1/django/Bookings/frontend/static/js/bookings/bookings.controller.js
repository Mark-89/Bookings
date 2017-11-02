myApp.controller('MainCtrl', function($modal, $scope, bookingsService, bookingsFactory) {
      
    var self = this;    
    self.bookings = [];
    
    self.currentPage = 1;
    self.previous = null;
    self.next = null;
    
    self.goToPreviousPage = function goToPreviousPage() {
        if (self.previous != null) {
            self.currentPage -= 1;
            getBookings(self.currentPage);
        }
    };
    
    self.goToNextPage = function goToNextPage() {
        if (self.next != null) {
            self.currentPage += 1;
            getBookings(self.currentPage);
        }
    };
    
    self.openBookingInfoModal = function openInfo(booking) {
        var modalInstance = $modal.open({
            size: "lg",
            templateUrl: "bookingInfoModal/bookingInfoModal.html",
            controller: "bookingInfoController",
            controllerAs: "vm",
            backdrop: "static",
            resolve: {
                booking: function() {
                    return booking;
                }
            }   
        });
    };
 
    function getBookings(page) {
        bookingsService.getBookings(page)
        .then(function (serverData) {
                self.bookings = serverData.results;
                self.previous = serverData.previous;
                self.next = serverData.next;
      });
       
    }      
  
      
    function activate() {
       getBookings(self.currentPage)
      }
      
      activate();
});