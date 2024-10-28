from django.contrib import admin

# Register your models here.
from .models import News
from .models import Category, Venue, MyClubUser, Event, City
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event_date', 'venue', 'manager', 'city', 'approved')
    list_display_links = ('name',)
    list_editable = ('approved',)
    search_fields = ('name',)
    list_filter = ('event_date',)

class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('last_name',)
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(MyClubUser, MyClubUserAdmin)
admin.site.register(City, CityAdmin)