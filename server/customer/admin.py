from django.contrib import admin
from .models import Customer, Country, Position


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'country', 'position', 'email')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')