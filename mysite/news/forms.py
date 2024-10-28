from django import forms
from django.forms import ModelForm
from .models import Category, Venue, City, News, Event


class NewsForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Выбери категорию")

    class Meta:
        model = News
        fields = ("title", "content", "category", "photo")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи заголовок'}),
        }


class VenueForm(ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label= "Выбери город", label="")
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'city', 'phone', 'web', 'email_address', 'venue_photo')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
            'venue_photo': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи название места'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи адрес'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи почтовый индекс'}),
            'phone': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Введи номер телефона'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи веб-сайт'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи электронную почту'}),
        }

class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'city', 'manager', 'description', 'attendees', 'photo_event')
        labels = {
            'name': '',
            'event_date': 'ДД-ММ-ГГ ЧЧ:ММ:СС',
            'venue': 'Выберите локацмю',
            'manager': 'Выберите менеджера',
            'description': '',
            'attendees': '',
            'city': 'Выберите город',
            'photo_event': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи название мероприятия'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Выберите дату и время мероприятия', 'type': 'datetime-local'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выбери место проведения'}),
            'city': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выбери город'}),
            'manager': forms.Select(attrs ={'class': 'form-select', 'placeholder': 'Выбери менеджера'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введи текст'}),
            'attendees': forms.SelectMultiple   (attrs={'class': 'form-control', 'placeholder': 'Выбери приглашенных'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'city', 'description', 'attendees')
        labels = {
            'name': '',
            'event_date': 'ДД-ММ-ГГ ЧЧ:ММ:СС',
            'venue': 'Выберите локацмю',
            'description': '',
            'attendees': '',
            'city': 'Выберите город',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи название мероприятия'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи дату'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выбери место проведения'}),
            'city': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Выбери город'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введи текст'}),
            'attendees': forms.SelectMultiple   (attrs={'class': 'form-control', 'placeholder': 'Выбери приглашенных'}),
        }

