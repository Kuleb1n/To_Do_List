from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from to_do.models import ToDoListTitle, Record


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ToDiListCreateForm(ModelForm):
    class Meta:
        model = ToDoListTitle
        fields = ['title', 'user']


class RecordCreateForm(ModelForm):
    class Meta:
        model = Record
        fields = ['record_title', 'status', 'title']
