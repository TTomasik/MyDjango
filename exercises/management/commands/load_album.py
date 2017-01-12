from django.core.management import BaseCommand
from django.utils import timezone
from exercises.models import Band, Album
    
#MOJE:
def album():
    Album.objects.update_or_create(title="ALBUM1-parser", year=2010, rating=2)
    Album.objects.update_or_create(title="ALBUM2-parser", year=2011, rating=3)
    Album.objects.update_or_create(title="ALBUM3-parser", year=2016, rating=4)

  
def print_hello():
    print("HELLO W FUNKCJI")    

class Command(BaseCommand):
    help = 'Initialize database'

    def add_arguments(self, parser):
        parser.add_argument('--add-album',
                            action='store_true',
                            dest='add-album',
                            default=False,
                            help='Insert album data') 
    
        parser.add_argument('--hello',
                            action='store_true',
                            dest='hello',
                            default=False,
                            help='Print hello') 
    

    def handle(self, *args, **options):
        start = timezone.now()
        print("TO JEST COS PO CZYM POWINNO SIE WYSWIETLIC")
        update_all = not any([options['add-album'], options['hello']])

        if options['add-album'] or update_all:
            print("LOADING ALBUMS...")
            album()
            
        if options['hello'] or update_all:
            print("HELLLOOOO!!!!")
            print_hello()
            

        end = timezone.now()
        print(end - start)