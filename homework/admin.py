from django.contrib import admin
from homework.models import Person, Movie, Role
   
@admin.register(Person)
class PersonInfo(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
       
@admin.register(Movie)
class MovieInfo(admin.ModelAdmin):
    list_display = ('title', 'director')

@admin.register(Role)
class RoleList(admin.ModelAdmin):
    list_display = ('role', 'person', 'movie')