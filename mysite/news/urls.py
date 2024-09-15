from django.urls import path
from .views import *
from .views import home

urlpatterns = [
    path('', index, name="home"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('news_item/<int:news_id>/', view_news, name="view_news"),
    path('add_news', add_news, name = "add_news"),
    path('<int:year>/<str:month>', home, name = "name"),
    path('events', event, name= "event"),
    path('add_venue', add_venue, name="add_venue"),
    path('city/<int:city_id>/', get_city, name='city'),
    path('venue/city/<int:city_id>/', get_city_2, name='city_2'),
    path('venue', venue, name="venue"),
    path('show_search', show_search, name='show_search')
]