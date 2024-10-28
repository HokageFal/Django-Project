from django.urls import path
from .views import *
from .views import home

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('news_item/<int:news_id>/', view_news, name="view_news"),
    path('add_news', add_news, name = "add_news"),
    path('<int:year>/<str:month>', home, name = "name"),
    path('events/<event_id>/', view_event, name= "view_event"),
    path('events', event, name="event"),
    path('add_venue', add_venue, name="add_venue"),
    path('city/<int:city_id>/', get_city, name='city'),
    path('venue/city/<int:city_id>/', get_city_2, name='city_2'),
    path('venue', list_venues, name="venue"),
    path('show_search', show_search, name='show_search'),
    path('update_venue/<venue_id>', update_venue, name="update-venue"),
    path('update_event/<event_id>', update_event, name="update_event"),
    path('add_event', add_event, name="add_event"),
    path('delete_event/<event_id>', delete_event, name="delete_event"),
    path('delete_venue/<venue_id>', delete_venue, name="delete_venue"),
    path('venue_text', venue_text, name="venue_text"),
    path('venue_csv', venue_csv, name="venue_csv"),
    path('my_events', my_events, name="my_events"),
    path("admin_approved", admin_approved, name="admin_approved")

]