myApp.controller('MainCtrl', function($modal, $scope, bookingsService, bookingsFactory) {
      
    var self = this;  
      
    self.bookings = [];    
    self.currentPage = 1;
    self.previous = null;
    self.next = null;
    self.filterOptions = {
        1: "Search booking id",
        2: "Search space name",
        3: "Search product name",
        4: "Search venue name",
        5: "Search booker name"
    };
    self.selectedFilterOption = 1;
    self.searchText = null;
    
    
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
    
    self.search = function search() {         
              
        var searchObject;
                      
        switch(self.selectedFilterOption) {
            case 1:
                searchObject = {
                    bookingId: self.searchText
                    }
                    break;
            case 2:
             searchObject = {
                    spaceName: self.searchText
                    }
                    break;
            case 3:
             searchObject = {
                    productName: self.searchText
                    }
                    break;
            case 4:
             searchObject = {
                    venueName: self.searchText
                    }
                    break;
            case 5:
             searchObject = {
                    bookerName: self.searchText
                    }
                    break;
        }
          
        bookingsService.searchBookings(searchObject)
        .then(function (serverData) {
            self.openBookingInfoModal(serverData);               
      });
    }
    
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