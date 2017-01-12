from django.http import HttpResponse
from django.http import request
from exercises.models import Article, Band, MUSIC_TYPES, RATES, Person, Pizza, Category
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
import operator
import functools
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import UpdateView
from exercises.forms import SearchBandForm, PersonForm, ExerciseThree, PizzaForm, NextBand, Login, ProfileForm, Logg, addUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

@login_required
def list_articles(request):
    cont = dict() # zamiast dict() mozna dac {} - chodzi o pusty slownik
    cont['articles'] = Article.objects.filter(status=2)
    # cont = {'articles: Article.objects.filter(status=2} to wyzej mozna zapisac tak
    return render(request, 'exercises/list_articles.html', cont)

def index(request):
    cont = {}
    return render(request, 'exercises/base.html', cont)
    
def show_band(request, band_id):
    cont = dict()
    band = Band.objects.get(id=band_id)
    cont['band'] = band
    cont['miusic_type'] = dict(MUSIC_TYPES).get(band.genre)

    albumsObj = band.album_set.all()
    albums = list()
    for a in albumsObj:
         d = dict()
         d['title'] = a.title
         d['publication_date'] = a.year
         d['rate'] = dict(RATES).get(a.rating)
         albums.append(d)

    cont['albums'] = albums
    return render(request, 'exercises/show_band.html', cont)

def search_bands_objects(name, year=1900):
    bands = list()
    bands_obj = list()
    if name:
        if not year:
            year = 1900
        bands_obj = Band.objects.filter(functools.reduce(operator.or_,
                                                         [Q(name__icontains=q) for q in name.split()]
                                                         ), year__gte=year)
    else:
        if year:
            bands_obj = Band.objects.filter(year__gte=year)

    for a in bands_obj:
        d = dict()
        d['name'] = a.name
        d['year'] = a.year
        d['genre'] = dict(MUSIC_TYPES).get(a.genre)
        bands.append(d)

    return bands


@csrf_protect
def search_band(request):
    if request.method == 'POST':
        form = SearchBandForm(request.POST)
        bands = list()
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            bands = search_bands_objects(name, year)
            # return HttpResponseRedirect('/search_band/')
        return render(request,
                      'exercises/search_band.html',
                      {'bands': bands,
                       'form': form})
    else:
        form = SearchBandForm()
        return render(request,
                      'exercises/search_band.html',
                      {'form': form})
        
        
class SearchBandFormView(View):
    def get(self, request):
        form = SearchBandForm()
        return render(request,
                      'exercises/search_band_new.html',
                      {'form': form})

    def post(self, request):
        form = SearchBandForm(request.POST)
        bands = list()
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            bands = search_bands_objects(name, year)
            # return HttpResponseRedirect('/search_band/')
        return render(request,
                      'exercises/search_band_new.html',
                      {'bands': bands,
                       'form': form})
            
def thanks(request):
    return render(request, 'exercises/thanks.html')


class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'tool']
    success_url = '/thanks/'


class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'tool']
    template_name_suffix = '_form'
    success_url = '/thanks/'


class PersonDelete(DeleteView):
    model = Person
    fields = ['name']
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('thanks', current_app='exercises')

class MyPerson(View):
    def get(self, request, person_id):
        p = Person.objects.get(pk=person_id)
        form = PersonForm(instance=p)
        return render(request, "exercises/person_form.html", {"form": form})

    def post(self, request, person_id):
        p = Person.objects.get(pk=person_id)
        form = PersonForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
        return render(request, "exercises/person_form.html", {"form": form})

class ExerciseThreeForm(View):
    def get(self, request):
        form = ExerciseThree()
        return render(request,
                      'exercises/ex_three.html',
                      {'form': form})

    def post(self, request):
        form = ExerciseThree(request.POST)
        data = []
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            year = form.cleaned_data['year']
            data = (name, surname, year)
        return render(request,
                      'exercises/ex_three.html',
                      {'data': data,
                       'form': form})

# JESZCZE TRZEBA ZROBIC DRUGA CZESC ZADANIA CZYLI METODE POST

# class SearchBandFormView(View):
#     def get(self, request):
#         form = SearchBandForm()
#         return render(request,
#                       'exercises/search_band_new.html',
#                       {'form': form})
#
    # def post(self, request):
    #     form = SearchBandForm(request.POST)
    #     bands = list()
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         year = form.cleaned_data['year']
    #         bands = search_bands_objects(name, year)
    #         # return HttpResponseRedirect('/search_band/')
    #     return render(request,
    #                   'exercises/search_band_new.html',
    #                   {'bands': bands,
    #                    'form': form})

class PizzaView(View):
    def get(self, request, pizza_id):
        p = Pizza.objects.get(pk=pizza_id)
        form = PizzaForm(instance=p)
        return render(request, "exercises/pizza_form.html", {"form": form})

    def post(self, request, pizza_id):
        p = Pizza.objects.get(pk=pizza_id)
        form = PizzaForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
        return render(request, "exercises/pizza_form.html", {"form": form})

class NextBandView(View):
    def get(self, request):
        form = NextBand()
        return render(request, "exercises/next_band.html", {"form": form})

    def post(self, request):
        form = NextBand(request.POST)
        if form.is_valid():
            form.save()
        form = NextBand()
        return render(request, "exercises/next_band.html", {"form": form})

class CheckLogin(View):
    def get(self, request):
        form = Login()


        return render(request, "exercises/login.html", {"form": form})


    def post(self, request):
        form = Login(request.POST)

        if form.is_valid():
            return render(request, "exercises/login2.html", {"form": form})
        else:
            return render(request, "exercises/login3.html", {"form": form})



class ProfileView(FormView):
    template_name = 'exercises/profile_form.html'
    form_class = ProfileForm
    #success_url = '/thanks/'

    def form_valid(self, form):
        d = dict()
        d['name'] = form.cleaned_data['name']
        d['surname'] = form.cleaned_data['surname']
        d['www'] = form.cleaned_data['www']
        d['email'] = form.cleaned_data['email']
        return render(None, 'exercises/profile_form.html', {"data": d})

    def form_invalid(self, form):
        form.add_error(None, "ERRRRORO-1!")
        return super(ProfileView, self).form_invalid(form)


class Profile2View(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "exercises/profile_form.html", {"form": form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            d = dict()
            d['name'] = form.cleaned_data['name']
            d['surname'] = form.cleaned_data['surname']
            d['www'] = form.cleaned_data['www']
            d['email'] = form.cleaned_data['email']
            d['aaa'] = request.POST.get('aaa')
            return render(request, "exercises/profile_form.html", {"data": d})
        else:
            form.add_error(None, "ERRRRORO-2!")
            return render(request, "exercises/profile_form.html", {"form": form})

class CheckLog(View):
    def get(self, request):
        form = Logg()
        return render(request, "exercises/login.html", {"form": form})

    def post(self, request):
        form = Logg(request.POST)
        next = request.GET.get('next')

        if form.is_valid():
            l = form.cleaned_data['login']    # to jest druga metoda, mozna form=Login(request.POST) i l = from.cleaned_data['login'] password to samo
            p = form.cleaned_data['password']
        else:
            return HttpResponse("Błąd!")
        user = authenticate(username=l,
                            password=p)

        form = Logg()
        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
            else:
                return render(request, "exercises/login.html", {"form": form})
        # przekierowanie dalej
        else:
            # return render(request, "exercises/login.html", {"form": form})
            return HttpResponse("Nie prawidłowy login lub hasło!")

class MyLogin(View):
    def get(self, request):
        form = Logg()
        return render(request, "exercises/logger.html", {"form": form})


    def post(self, request):

        u = request.POST['login']
        p = request.POST['password']

        user = authenticate(username=u,
                        password=p)
        if user is not None:
            login(request, user)
            return render(request, "exercises/logger.html")
        else:
            return HttpResponse("Nie prawidłowy login lub hasło!")

class MyLogout(View):
    def get(self, request):
        logout(request)
        return render(request, "exercises/logger_out.html")


# LoginRequiredMixin -> to zamiast UserPassesTestMixin i sprawdza czy ktos jest zalogowany

class AddUser(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = addUser()
        return render(request, "exercises/new_user.html", {"form": form})

    def post(self, request):
        form = addUser(request.POST)
        if form.is_valid():

            user1 = form.cleaned_data['login']
            pw = form.cleaned_data['password']
            first = form.cleaned_data['name']
            last = form.cleaned_data['surname']
            em = form.cleaned_data['email']

            User.objects.create(
                username = user1,
                password = pw,
                first_name = first,
                last_name = last,
                email = em,
            )

        form = addUser()
        return render(request, "exercises/new_user.html", {"form": form})


class LoginExam(View):
    def get(self, request):
        form = Logg()
        return render(request, "exercises/login_exam.html", {"form": form})


    def post(self, request):

        u = request.POST['login']
        p = request.POST['password']

        user = authenticate(username=u,
                        password=p)
        if user is not None:
            login(request, user)
            return render(request, "exercises/login_exam.html")
        else:
            return HttpResponse("Nie prawidłowy login lub hasło!")








