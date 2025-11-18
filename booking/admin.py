from django.contrib import admin
from .models import Booking, Menu, Order
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_date', 'booking_time', 'number_of_people', 'user', 'booking_id')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('booking_date',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('booking', 'created_at')
