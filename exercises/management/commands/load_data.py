from django.core.management import BaseCommand
from django.utils import timezone
from exercises.models import Band, Album


def populate():
    Band.objects.update_or_create(name="The Beatles")
    Band.objects.update_or_create(name="The Rolling Stones")
    Band.objects.update_or_create(name="Metallica", year=1982)
    Band.objects.update_or_create(name="Pink Floyd", year=1965)
    Band.objects.update_or_create(name="Deep Purple")
    Band.objects.update_or_create(name="The Clash", year=1976)
    Band.objects.update_or_create(name="AC/DC", year=1973)
    Band.objects.update_or_create(name="Nirvana", year=1987)
    Band.objects.update_or_create(name="Blur", year=1988)
    Band.objects.update_or_create(name="Oasis", year=1991)
    Band.objects.update_or_create(name="Red Hot Chili Peppers", year=1983)
    Band.objects.update_or_create(name="System Of The Down", year=1994)
    Band.objects.update_or_create(name="Dire Straits")
    Band.objects.update_or_create(name="Twenty One Pilots", year=2009)
    Band.objects.update_or_create(name="Parser-example", year=2009)
    
#MOJE:
def addAlbum():
    Album.objects.update_or_create(name="The Beatles")
    Album.objects.update_or_create(name="The Rolling Stones")
    Album.objects.update_or_create(name="Metallica", year=1982)
    Album.objects.update_or_create(name="Pink Floyd", year=1965)
    Album.objects.update_or_create(name="Deep Purple")
  
    

class Command(BaseCommand):
    help = 'Initialize database'

    def add_arguments(self, parser):
        parser.add_argument('--add-bands',
                            action='store_true',
                            dest='add-bands',
                            default=False,
                            help='Insert band data')        
    

    def handle(self, *args, **options):
        start = timezone.now()

        update_all = not any([options['add-bands']])

        if options['add-bands'] or update_all:
            print("Loading bands...")
            populate()

        end = timezone.now()
        print(end - start)