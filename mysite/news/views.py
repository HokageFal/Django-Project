from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import News, Category, Event, Venue, City
from django.urls import reverse_lazy
from .forms import NewsForm, VenueForm

def venue(request):
    venue_list = Venue.objects.all()
    return render(request, 'news/venue.html', {'venue_list': venue_list})

def get_city_2(request, city_id):
    venue = Venue.objects.filter(city_id=city_id)
    city = City.objects.get(pk=city_id)
    return render(request, 'news/city_2.html', {'venue': venue, 'city': city})

def show_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'news/show_search.html',
                    {'searched': searched, 'venues': venues})
    else:
        return render(request, 'news/show_search.html', {})

def event(request):
    event_list = Event.objects.all()
    return render(request, 'news/event.html', {"event_list": event_list})

def get_city(request, city_id):
    event = Event.objects.filter(city_id=city_id)
    city = City.objects.get(pk=city_id)
    return render(request, 'news/city.html', {'event_list': event, 'city': city})

# Контроллеры
def index(request):
    # print(dir(request))
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'mysite',
    }
    return render(request, 'news/index.html', context=context)


def home(request, year, month):
    name = "Job"
    return render(request, "news/home.html", {"name": name, "year": year, "month": month})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    news = News.objects.filter(news_id=news_id)
    return render(request, 'news/view_news.html', {'news': news})

# class add_venue(CreateView):
#     model = Venue
#     form_class = VenueForm
#     template_name = 'news/add_venue.html'
#
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return HttpResponseRedirect('<h1>Вы отправили форму<h1>')
#


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'news/add_venue.html', {"form": form, "submitted": submitted})

def add_news(request):
    submitted = False
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            return HttpResponseRedirect('/add_news?submitted=True')
    else:
        form = NewsForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "news/add_news.html", {'form': form, "submitted": submitted})
