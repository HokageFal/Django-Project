from django import forms
from django.forms import ModelForm
from .models import Category, Venue, City, News


class NewsForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Выбери категорию")

    class Meta:
        model = News
        fields = ("title", "content", "category")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введи текст', 'rows': 5}),
        }


class VenueForm(ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label= "Выбери город", label="")
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'city', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи название места'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи адрес'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи почтовый индекс'}),
            'phone': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Введи номер телефона'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи веб-сайт'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введи электронную почту'}),
        }
