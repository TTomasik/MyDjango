from django.contrib import admin
from exercises.models import Band, Category, Article, Album, Song, Person, Position, Tool, Pizza, Topping, Profile


# Register your models here.
# admin.site.register(Band)

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    
@admin.register(Category)
class Categories(admin.ModelAdmin):
    list_display = ('name', 'description')
    
@admin.register(Article)
class Arts(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'date_added')
    
@admin.register(Album)    
class AlbumDisplay(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating')
    
@admin.register(Song)    
class Songs(admin.ModelAdmin):
    list_display = ('title', 'duration')
    
@admin.register(Person)    
class PersonPosition(admin.ModelAdmin):
    list_display = ('name', )
       
@admin.register(Position)      
class PositionName(admin.ModelAdmin):
    list_display = ('position_name', 'salary')
 
@admin.register(Tool)     
class PersonTool(admin.ModelAdmin):
    list_display = ('name', )

def send_pizza(model_admin, request, query_set):
    query_set.update(sent_to_customer=True)

send_pizza.short_description = "Wyślij pizze do klienta"


#admin.site.register(Pizza)
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'size', 'Toppings', "sent_to_customer")
    actions = [send_pizza, ]

    def Toppings(self, pizza):
        return ", ".join([t.name for t in pizza.toppings.all()])

@admin.register(Topping)
class Toppings(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'salary')
      
     
    
    
    
    