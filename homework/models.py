from django.db import models    
 
    
RANKS = (
    (0, "not define"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")   
)
    
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)       
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey('Person', related_name='movie_director')
    screenplay = models.ForeignKey('Person', related_name='movie_screenplay')
    starring = models.ManyToManyField('Person', through='Role', blank=True)
    year = models.SmallIntegerField()
    ranking = models.IntegerField(choices=RANKS, default=0)
        
    def __str__(self):
        return self.title
        
class Role(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="Movie") 
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="Movie")
    role = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.role
     
 
 
 
        
       