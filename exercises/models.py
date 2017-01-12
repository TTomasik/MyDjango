from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.mixins import PermissionRequiredMixin


MUSIC_TYPES = (
    (-1, "not defined"),
    (0, "rock"),
    (1, "metal"),
    (2, "pop"),
    (3, "hip-hop"),
    (4, "eletronic"),
    (5, "regge"),
    (6, "other") 
)

RATES = (
    (0, ""),
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****")
)

ARTICLE_STATUS = (
    (0, "working on"),
    (1, "almost done"),
    (2, "done")

)
# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=MUSIC_TYPES, default=-1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together=('name', 'year')
    
class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    content = models.TextField(null=True)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)
#    date_added = models.DateTimeField(auto_now_add=True)  """TO JEST ALTERNATYWA DLA TEGO CO NA GORZE"""
    status = models.IntegerField(choices=ARTICLE_STATUS, default=0)
    emission_start = models.DateField(null=True)
    emission_end = models.DateField(null=True) 
    category = models.ManyToManyField('Category')     
    
    def __str__(self):
        return self.title
    
class Album(PermissionRequiredMixin, models.Model):
    permission_required = 'exercises.add_album'
    title = models.CharField(max_length=128, unique=True)
    year = models.IntegerField(null=True)
    # ,validators = [MaxValueValidator(2100), MinValueValidator(1900)] doklejam to za null=True -> powyzej
    rating = models.IntegerField(choices=RATES, default=0)
    band = models.ForeignKey('Band', null=True)
    song = models.ForeignKey('Song', null=True)



    
    def __str__(self):
        return self.title
    
#    filtered = Band.objects.all(year__isnull="True").update(year="1900")

class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.DurationField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    


class Person(models.Model):
    name = models.CharField(max_length=64)
    tool = models.ManyToManyField('Tool', blank=True)
    
    def __str__(self): # powinno wyświetlić tytuł w formie stringa
        return self.name

class Position(models.Model):   
 
    person = models.OneToOneField('Person', on_delete=models.CASCADE, primary_key=True)
    salary = models.DecimalField(default=0.0, decimal_places=2, max_digits=7)   
    position_name=models.CharField(max_length=64)
 
    def __str__(self): # powinno wyświetlić tytuł w formie stringa
        return '%s is %s' % (self.person.name, self.position_name) 

class Tool(models.Model):
    name = models.CharField(max_length=64)
     
    def __str__(self):
        return self.name

PIZZA_SIZES = (
    (1, "small"),
    (2, "medium"),
    (3, "big"),)


class Topping(models.Model):
    name = models.CharField(max_length=32,
                            verbose_name="nazwa dodatku",
                            help_text="Podaj nazwę dodatku (bez opisu)")
    price = models.FloatField(verbose_name="cena",
                              help_text="cena dodatku dodawana jest do ceny pizzy")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES, verbose_name='rozmiar')
    toppings = models.ManyToManyField(Topping, blank=True, verbose_name='dodatki')
    sent_to_customer = models.BooleanField(default=False, verbose_name='Wysłana do klienta?')

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizze'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return '%s is %s' % (self.user.name, self.salary)




# class UpgradeUser(AbstractUser):
#     type = models.CharField(max_length=32)
#     calories = models.FloatField()
#     weight = models.FloatField()
    
    
    
    
    
    


