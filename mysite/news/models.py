from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование новости')
    content = models.TextField(blank=True, verbose_name='Контент') #Необазетельно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') # Просмотр даты редактирования новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class City(models.Model):
    title = models.CharField(max_length=120, db_index=True)

    def get_absolute_url(self):
        return reverse('city', kwargs={'city_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip code', max_length=15)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)
    owner = models.IntegerField("Venue Owner", blank=False, default=1)
    venue_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место проведения'
        ordering = ['-name']

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Name')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['first_name']

class Event(models.Model):
    name = models.CharField("Venue name", max_length=120)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, max_length=120, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True)
    photo_event = models.ImageField(blank=True)
    approved = models.BooleanField("Опубликовать/одобрить", default = False)

    def get_absolute_url(self):
        return reverse('view_event', kwargs={'event_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-event_date']

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        return days_till
        # return str(self.event_date.date()).split(",", 1)[0]
        # return today