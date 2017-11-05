from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from api.models import Bookings
from api.models import Items
from api.models import Venues
from api.models import BookingItems
from api.models import Users
from api.models import Bookers
from api.serializers import BookingsSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

           
@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def bookings_list(request):
    """
    List all bookings.
    """
    if request.method == 'GET':       
        bookings = Bookings.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(bookings, request)
        serializer = BookingsSerializer(result_page, many = True)     
        return paginator.get_paginated_response(serializer.data)   
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET'])
def bookings_search(request):
    """
    Search the bookings.
    """
    if 'bookingId' in request.GET:
        bookingId = request.GET.get('bookingId', '')
        bookings = get_list_or_404(Bookings, id = bookingId)
        
    elif 'spaceName' in request.GET:
        spaceName = request.GET.get('spaceName', '')
        item = get_object_or_404(Items, name = spaceName)      
        bookingItems = BookingItems.objects.filter(item = item.id)
        bookingId_list = bookingItems.values_list('booking', flat = True)
        bookings = Bookings.objects.filter(id__in=bookingId_list)  
              
    elif 'productName' in request.GET:
        productName = request.GET.get('productName', '')
        item = get_object_or_404(Items, name=productName)      
        bookingItems = BookingItems.objects.filter(item = item.id)
        bookingId_list = bookingItems.values_list('booking', flat = True)     
        bookings = Bookings.objects.filter(id__in=bookingId_list) 
               
    elif 'venueName' in request.GET:
        venueName = request.GET.get('venueName', '')
        venue = get_object_or_404(Venues, name = venueName)       
        items = Items.objects.filter(venue = venue.id)
        itemsId_list = items.values_list('id', flat = True)
        bookingItems = BookingItems.objects.filter(item__in = itemsId_list)
        bookingId_list = bookingItems.values_list('booking', flat = True)     
        bookings = Bookings.objects.filter(id__in = bookingId_list)  
          
    elif 'bookerName' in request.GET:
        bookerName = request.GET.get('bookerName', '')
        users = Users.objects.filter(Q(first_name__icontains = bookerName) | Q(last_name__icontains = bookerName) | Q(email__icontains=bookerName))
        usersId_list = users.values_list('id', flat = True)
        bookers = Bookers.objects.filter(user__in = usersId_list)
        bookersId_list = bookers.values_list('id', flat = True)
        bookings = Bookings.objects.filter(booker__in = bookersId_list)

    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(bookings, request)
    serializer = BookingsSerializer(result_page, many = True)

    return paginator.get_paginated_response(serializer.data)