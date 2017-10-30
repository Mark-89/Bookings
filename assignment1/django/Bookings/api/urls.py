from django.conf.urls import url, include
#from api.views import products_list
from api.views import bookings_list

urlpatterns = [    
    #url(r'^products/$', products_list, name='products_list'),
    url(r'^bookings/$', bookings_list, name='bookings_list'), 
    url(r'^', include('frontend.urls', namespace='frontend')),     
]