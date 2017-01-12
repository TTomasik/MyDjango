from django.shortcuts import render
from django.views import View
from homework.models import Movie, Role, Person
from homework.forms import NewPerson
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ShowMovies(View):

    def get(self, request):
        cont = {}
        movieObj = Movie.objects.all()
        MOVIES = []

        for m in movieObj:
            d = {}
            d['id'] = m.id
            d['title'] = m.title
            d['year'] = m.year
            d['director'] = m.director
            MOVIES.append(d)

        cont['movies'] = MOVIES

        return render(request, 'movie.html', cont)

class MovieDetails(View):

    def get(self, request, movie_id):

        cont = {}
        movie = Movie.objects.get(id=movie_id)
        cont['movie'] = movie

        actorsOBJ = Movie.objects.get(id=movie_id).starring.all()

        ACTORS = []

        for c in actorsOBJ:
            # person = Movie.objects.get(id=movie_id).starring.all()
            a = {}
            a['first_name'] = c.first_name
            a['last_name'] = c.last_name
            a['role'] = Role.objects.filter(person__in=[c])[0].role

            ACTORS.append(a)

        cont['actors'] = ACTORS


        return render(request, 'movie_details.html', cont)

# per = Person.objects.all[i]
# Movie.objects.filter(starring__in=[per])
#
# mov = Movie.objects.all()[movie_id]
# Role.objects.filter(movie__in=[mov])
#
# Movie.objects.get(id=4).starring.all()[0] -> emma
# Role.objects.filter(person__in=[emma])

class People(View):

    def get(self, request):
        cont = {}
        peopleObj = Person.objects.all()
        PEOPLE = []

        for m in peopleObj:
            d = {}
            d['first_name'] = m.first_name
            d['last_name'] = m.last_name
            # d['movie'] = Movie.objects.filter(starring__in=[m])
            d['id'] = m.id

            PEOPLE.append(d)

        cont['persons'] = PEOPLE

        return render(request, 'people.html', cont)

# class NewPersonView(View):
#     def get(self, request):
#         form = NewPerson()
#         return render(request, "new_person.html", {"form": form})
#
#     def post(self, request):
#         form = NewPerson(request.POST)
#         if form.is_valid():
#             form.save()
#         form = NewPerson()
#         return render(request, "new_person.html", {"form": form})

class PersonCreator(CreateView):
    model = Person
    fields = '__all__'
    success_url = '/people/'


class PersonUpdater(UpdateView):
    model = Person
    fields = '__all__'
    success_url = '/people/'

class MovieUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'homework.change_movie'
    model = Movie
    fields = '__all__'
    success_url = '/movie_edit/'

class MovieDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'homework.delete_movie'
    model = Movie
    fields = '__all__'
    template_name_suffix = '_delete_form'
    success_url = '/movies/'

class MovieCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'homework.add_movie'
    model = Movie
    fields = '__all__'
    success_url = '/movie_add/'