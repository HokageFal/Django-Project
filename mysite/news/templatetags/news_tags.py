from django import template

from news.models import Category, City, Venue

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_citye():
    return City.objects.all()


