from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import News, Category, Event, Venue, City
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import NewsForm, VenueForm, EventForm, EventFormAdmin
import csv
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def admin_approved(request):
    event_count = Event.objects.all().count()
    venue_count = Venue.objects.all().count()
    user_count = User.objects.all().count()
    events = Event.objects.all().order_by('-event_date')
    if request.user.is_superuser:
        if request.method == "POST":
            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')

            # Uncheck all events
            events.update(approved=False)

            # Update the database
            for x in id_list:
                Event.objects.filter(pk=int(x)).update(approved=True)

            # Show Success Message and Redirect
            messages.success(request, ("Мероприятия обновлены"))
            return redirect('event')



        else:
            return render(request, 'news/admin_approved.html',
                          {"events": events,
                           "event_count": event_count,
                           "venue_count": venue_count,
                           "user_count": user_count
                           })
    else:
        messages.success(request, ("У вас нет прав для захода в эту страницу"))
        return redirect('home')


def my_events(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(attendees=request.user.id)
        return render(request, "news/my_events.html", {'events': events})
    else:
        messages.success(request, ("Вы не вошли в учетную запись"))
        return redirect("login")


def list_venues(request):
	#venue_list = Venue.objects.all().order_by('?')
	venue_list = Venue.objects.all()
	# Set up Pagination
	p = Paginator(Venue.objects.all(), 5)
	page = request.GET.get('page')
	venues = p.get_page(page)
	nums = "a" * venues.paginator.num_pages
	return render(request, 'news/venue.html',
		{'venue_list': venue_list,
		'venues': venues,
		'nums':nums}
		)


def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    venues = Venue.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])

    # Loop Thu and output
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

    return response

def venue_text(request):
    responce = HttpResponse(content_type="text/plain")
    responce["Content-Disposition"] = "attachment; filename=venues.txt"
    venue_list = Venue.objects.all()
    lines = []

    for venue in venue_list:
        lines.append(f"{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.city}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n")
    responce.writelines(lines)
    return responce

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        messages.success(request, ("Мероприятие было удалено"))
        event.delete()
        return redirect("event")
    else:
        messages.success(request, ("У вас нет полномочий для удаления данного мероприятия"))
        return redirect("event")

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect("venue")


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect("event")
    return render(request, 'news/update_event.html', {"event": event, "form": form})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect("venue")
    return render(request, 'news/update_venue.html', {"venue": venue, "form": form})


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
    event_list = Event.objects.all().order_by("name")
    return render(request, 'news/event.html', {"event_list": event_list})

def view_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'news/view_event.html', {'event': event})

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


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue =  form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
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
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted = True
            return HttpResponseRedirect('/add_news?submitted=True')
    else:
        form = NewsForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "news/add_news.html", {'form': form, "submitted": submitted})

def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted = True
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.manager = request.user
                event.save()
                submitted = True
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'news/add_event.html', {"form": form, "submitted": submitted})