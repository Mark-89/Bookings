myApp.controller('bookingInfoController', function($modalInstance, booking) {
    var self = this;
    
    self.booking = booking;
    
    self.close = function close() {
        $modalInstance.close();
    }
});
      