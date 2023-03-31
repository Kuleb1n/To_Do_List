from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from to_do.forms import *
from to_do.models import ToDoListTitle, Record


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserAuthenticationForm

    def get_success_url(self):
        return reverse('to-do-list')


class UserCreateView(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserRegistrationForm

    def get_success_url(self):
        return reverse('login')


class ToDoListView(CreateView, ListView):
    model = ToDoListTitle
    template_name = 'to-do-list.html'
    form_class = ToDiListCreateForm
    context_object_name = 'to_do_list'
    success_url = reverse_lazy('to-do-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ToDoListView, self).get_context_data()
        context['records'] = Record.objects.all().select_related()
        return context


def to_do_list_delete(request, pk_to_do_list):
    to_do_list = ToDoListTitle.objects.get(pk=pk_to_do_list)
    to_do_list.delete()

    return redirect('to-do-list')


class RecordView(CreateView, ListView):
    model = Record
    template_name = 'to-do-list.html'
    form_class = RecordCreateForm
    success_url = reverse_lazy('to-do-list')


def record_delete(request, pk_record):
    record = Record.objects.get(pk=pk_record)
    record.delete()

    return redirect('to-do-list')


def record_update(request, pk_record):
    record = Record.objects.get(pk=pk_record)
    record.status = True
    record.save()

    return redirect("to-do-list")


def user_logout(request):
    logout(request)
    return redirect('login')
