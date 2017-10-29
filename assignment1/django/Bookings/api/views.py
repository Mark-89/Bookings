#from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from api.models import Products
from api.models import Bookings
from api.serializers import BookingsSerializer
from rest_framework.pagination import PageNumberPagination



#@api_view(['GET', 'POST'])
#@api_view(['GET'])
#def products_list(request):
#    """
#    List all products.
#    """
#    if request.method == 'GET':
#        products = Products.objects.all()
#        serializer = BookingsSerializer(products, many=True)
#        return Response(serializer.data)
#   
#    else:
#        return Response(
#            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
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