# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Venues(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'venues'


class Items(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    venue = models.ForeignKey(Venues, models.DO_NOTHING)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.Items_id

    class Meta:
        managed = False
        db_table = 'items'
    
       

class Spaces(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    hour_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'spaces'


class Products(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registered = models.IntegerField()
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class Bookers(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookers'


class Bookings(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    booker = models.ForeignKey(Bookers, models.DO_NOTHING)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookings'


class BookingItems(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    booking = models.ForeignKey(Bookings, models.DO_NOTHING)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    quantity = models.IntegerField()
    locked_piece_price = models.FloatField()
    locked_total_price = models.FloatField()
    start_timestamp = models.IntegerField(blank=True, null=True)
    end_timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_items'