from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment, Client, Booking, Update

# Treatment
@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    """ TreatmentAdmin """
    list_filter = ('category', 'duration')
    list_display = ('title', 'category')
    search_fields = ['category', 'duration']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')

# Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """ ClientAdmin """
    list_filter = ('first_name', 'last_name', 'phone', 'email')
    list_display = ('first_name', 'last_name', 'phone', 'email')
    search_fields = ['first_name', 'last_name', 'phone', 'email']

# Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ BookingAdmin """
    list_filter = ('client', 'treatment', 'date_of_treatment', 'time_of_treatment')
    list_display = ('client', 'treatment', 'date_of_treatment', 'time_of_treatment', 'status')
    search_fields = ['client', 'treatment', 'date_of_treatment', 'time_of_treatment']
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status=1)


# Update Booking Request
@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    """ UpdateAdmin """
    list_filter = ('name', 'new_specification')
    list_display = ('name', 'new_specification')
    search_fields = ['name', 'new_specification']
