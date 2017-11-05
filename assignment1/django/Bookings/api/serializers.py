from rest_framework import serializers
from api.models import Bookings
from api.models import Bookers
from api.models import Users
from api.models import BookingItems
from api.models import Items
from api.models import Venues
from api.models import Products
from api.models import Spaces


class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email')


class VenuesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venues
        fields = ('id', 'name')


class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = ('id', 'item', 'price')


class SpacesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Spaces
        fields = ('id', 'item', 'hour_price')


class ItemsSerializer(serializers.ModelSerializer):
    venue = VenuesSerializer(many=False, read_only=True)
    products = ProductsSerializer(source='products_set', many=True)
    spaces = SpacesSerializer(source='spaces_set', many=True)
    
    class Meta:
        model = Items
        fields = ('id', 'venue', 'name', 'products', 'spaces')


class BookingItemsSerializer(serializers.ModelSerializer):
    item = ItemsSerializer(many=False, read_only=True)
    
    class Meta:
        model = BookingItems
        fields = ('id', 'booking', 'item')


class BookersSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False, read_only=True)
    
    class Meta:
        model = Bookers
        fields = ('id', 'user')


class BookingsSerializer(serializers.ModelSerializer):    
    booker = BookersSerializer(many=False, read_only=True)
    bookingitems = BookingItemsSerializer(source='bookingitems_set', many=True)

    class Meta:
        model = Bookings
        fields = ('id', 'booker', 'bookingitems')        