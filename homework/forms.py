from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, SelectMultiple, RadioSelect
from django.utils import timezone
from homework.models import Person



class NewPerson(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
