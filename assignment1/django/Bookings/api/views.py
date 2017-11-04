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
from api.serializers import UsersSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

           
@api_view(['GET'])
def bookings_list(request):
    """
    List all bookings.
    """
    if request.method == 'GET':
        #bookings = Bookings.objects.filter(id__in=[10065, 10066, 10077])
        #bookings = Bookings.objects.filter(booker__isnull=False)
        bookings = Bookings.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(bookings, request)
        serializer = BookingsSerializer(result_page, many=True)
        #return Response(serializer.data)
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
        
#    bookings = Bookings.objects.all()
        bookingId = request.GET.get('bookingId', '')
#        bookings = Bookings.objects.filter(id__in=[bookingId])
        bookings = get_list_or_404(Bookings, id=bookingId)
        
#    if request.method == 'GET':
#        products = Products.objects.all()
    elif 'spaceName' in request.GET:
        spaceName = request.GET.get('spaceName', '')
#        item = Items.objects.filter(name__in=[spaceName])
        item = get_object_or_404(Items, name=spaceName)
       
#        import pdb; pdb.set_trace()    
        
        bookingItems = BookingItems.objects.filter(item = item.id)
        bookingId_list = bookingItems.values_list('booking', flat=True)
#        bookingItem = get_object_or_404(BookingItems, item=item.id)
       
#        import pdb; pdb.set_trace()  
#        bookings = get_object_or_404(Bookings, pk=bookingItem.id)
#        bookings = Bookings.objects.get(id__in=[spaceName])
#        bookings = Bookings.objects.filter(id = 
        bookings = Bookings.objects.filter(id__in=bookingId_list)
        
    elif 'productName' in request.GET:
        productName = request.GET.get('productName', '')
        item = get_object_or_404(Items, name=productName)      
        bookingItems = BookingItems.objects.filter(item = item.id)
        bookingId_list = bookingItems.values_list('booking', flat=True)     
        bookings = Bookings.objects.filter(id__in=bookingId_list)
        
    elif 'venueName' in request.GET:
        venueName = request.GET.get('venueName', '')
        venue = get_object_or_404(Venues, name=venueName)
       
        items = Items.objects.filter(venue = venue.id)
#        import pdb; pdb.set_trace()
        itemsId_list = items.values_list('id', flat=True)
        bookingItems = BookingItems.objects.filter(item__in = itemsId_list)
        bookingId_list = bookingItems.values_list('booking', flat=True)     
        bookings = Bookings.objects.filter(id__in=bookingId_list)
    
    elif 'bookerName' in request.GET:
        bookerName = request.GET.get('bookerName', '')
#        usersQuery = Users.objects.filter(Q(first_name__icontains = bookerName) | Q(last_name__icontains = bookerName) | Q(email__icontains=bookerName))     
#        users = get_list_or_404(usersQuery)
        users = Users.objects.filter(Q(first_name__icontains = bookerName) | Q(last_name__icontains = bookerName) | Q(email__icontains=bookerName))
        usersId_list = users.values_list('id', flat = True)
        bookers = Bookers.objects.filter(user__in = usersId_list)
        bookersId_list = bookers.values_list('id', flat=True)
#        import pdb; pdb.set_trace()
        bookings = Bookings.objects.filter(booker__in =bookersId_list)
#        bla = UsersSerializer(users)
#        return Response(bla.data)
          
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(bookings, request)
    serializer = BookingsSerializer(result_page, many=True)
#    serializer = BookingItemsSerializer(bookingItems, many=True)
    return paginator.get_paginated_response(serializer.data)
#   
#    else:
#        return Response(
#            serializer.errors, status=status.HTTP_400_BAD_REQUEST)