"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from exercises.views import list_articles, index, show_band, search_band, SearchBandFormView, \
    thanks, PersonCreate, PersonUpdate, PersonDelete, MyPerson, ExerciseThreeForm, PizzaView, \
    NextBandView, CheckLogin, ProfileView, Profile2View, CheckLog, MyLogin, MyLogout, AddUser, LoginExam
from homework.views import ShowMovies, MovieDetails, People, PersonCreator, PersonUpdater, MovieUpdate, MovieDelete, MovieCreate
from django.contrib.auth.views import logout_then_login
from exercises.forms import PersonForm
 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/?$', list_articles, name="list_articles"),
    url(r'^logout/$', logout_then_login, name='site-logout'),
    url(r'^$', index, name='index'),
    url(r'^show_band/(?P<band_id>(\d){1,4})$', show_band, name="show_band"),    
    url(r'^search_band/?$', search_band, name='search-band'),
    url(r'^search_band_new/?$', SearchBandFormView.as_view(), name='search-band-new'),
    url(r'^movies/?$', ShowMovies.as_view(), name="movies-list"),
    url(r'^movie_details/(?P<movie_id>(\d){1,4})$', MovieDetails.as_view(), name="movie-details"),
    url(r'^thanks/?$', thanks, name='thanks'),
    url(r'^person_create/?$', PersonCreate.as_view(), name='person-create'),
    url(r'^person_update/(?P<pk>\d+)/?$', PersonUpdate.as_view(), name='person-update'),
    url(r'^person_delete/(?P<pk>\d+)/?$', PersonDelete.as_view(), name='person-delete'),
    url(r'^person_form/(?P<person_id>\d+)/?$', MyPerson.as_view(), name='person-form'),
    url(r'^exercise_three/?$', ExerciseThreeForm.as_view(), name='ex-three'),
    url(r'^pizza_form/(?P<pizza_id>\d+)/?$', PizzaView.as_view(), name='pizza-form'),
    url(r'^next_band/?$', NextBandView.as_view(), name='next-band'),
    url(r'^login/?$', CheckLogin.as_view(), name='login'),
    url(r'^people/?$', People.as_view(), name='people'),
    url(r'^new_person/?$', PersonCreator.as_view(), name='new-person'),
    url(r'^update_person/(?P<pk>\d+)/?$', PersonUpdater.as_view(), name='update-person'),
    url(r'^movie_edit/(?P<pk>\d+)/?$', MovieUpdate.as_view(), name='movie-update'),
    url(r'^movie_delete/(?P<pk>\d+)/?$', MovieDelete.as_view(), name='movie-delete'),
    url(r'^movie_add/?$', MovieCreate.as_view(), name='movie-add'),
    url(r'^profile_form/?$', ProfileView.as_view(), name='profile-form'),
    url(r'^profile_form2/?$', Profile2View.as_view(), name='profile2-form'),
    url(r'^log/?$', CheckLog.as_view(), name='log'),
    url(r'^logger$', MyLogin.as_view(), name='logger'),
    url(r'^logger_out$', MyLogout.as_view(), name='logger-out'),
    url(r'^new_user$', AddUser.as_view(), name='logger-out'),
    url(r'^login_exam', LoginExam.as_view(), name='login-exam'),
]
