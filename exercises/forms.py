from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple, RadioSelect
from django.utils import timezone
from exercises.models import Article, Band, MUSIC_TYPES, RATES, Person, Pizza




def validate_even(value):
    if value % 2 != 0:
        raise ValidationError("year %s is not even!" % value)


def validate_name(value):
    if value[-1] != 'a':
        raise ValidationError("'%s' is not a female name" % value)


class SearchBandForm(forms.Form):
    name = forms.CharField(
        label='Band name',
        max_length=148,
        # widget=forms.Textarea,
        widget=forms.TextInput,
        required=True,
    )
    year = forms.IntegerField(
        label='After year',
        min_value=1900,
        max_value=timezone.now().year,
        required=False,
        validators=[validate_even],
    )

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # # exclude = ['available_from', ]

class ExerciseThree(forms.Form):
    name = forms.CharField(
        label='Your name',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    surname = forms.CharField(
        label='Your surname',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    year = forms.IntegerField()

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['toppings', 'size']
        widgets = {
            'toppings': CheckboxSelectMultiple()
            # 'toppings': SelectMultiple()
        }

class NextBand(ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        widgets = {
            'genre': RadioSelect()
        }


def validate_login(login):
    if login != 'root':
        raise ValidationError("Login niepoprawny!")

def validate_password(password):
    if password != 'very_secret':
        raise ValidationError("Hasło niepoprawne!")


class Login(forms.Form):
    login = forms.CharField(
        label='Login',
        max_length=64,
        widget=forms.TextInput,
        required=True,
        validators=[validate_login],
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
        validators=[validate_password],
    )

class ArticleId(forms.Form):
    article_id = forms.IntegerField(
        widget=forms.HiddenInput,
    )

def validate_name(value):
    if value[-1] != 'a':
        raise ValidationError("'%s' is not a female name" % value)

class ProfileForm(forms.Form):
    name = forms.CharField(validators=[validate_name])
    surname = forms.CharField(required=False)
    www = forms.URLField()
    email = forms.EmailField()


class Logg(forms.Form):
    login = forms.CharField(
        label='Login',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )

class addUser(forms.Form):
    login = forms.CharField(
        label='Login',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label='Repeat password',
        max_length=64,
        widget=forms.PasswordInput,
        required=True,
    )
    name = forms.CharField(
        label='Name',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    surname = forms.CharField(
        label='Surname',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
    email = forms.CharField(
        label='Email',
        max_length=64,
        widget=forms.TextInput,
        required=True,
    )
