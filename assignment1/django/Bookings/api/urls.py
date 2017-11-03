from django.conf.urls import url, include
from api.views import bookings_list
from api.views import bookings_search

urlpatterns = [  
    url(r'^bookings/$', bookings_list, name='bookings_list'), 
    url(r'^bookings/search/$', bookings_search, name='bookings_search'), 
    url(r'^', include('frontend.urls', namespace='frontend')),     
]