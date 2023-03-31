from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('to-do-list/', login_required(ToDoListView.as_view()), name='to-do-list'),
    path('to-do-list/delete/<int:pk_to_do_list>', to_do_list_delete, name='to-do-list-delete'),
    path('add-record/', login_required(RecordView.as_view()), name='add-record'),
    path('record/delete/<int:pk_record>', record_delete, name='record-delete'),
    path('record/update/<int:pk_record>', record_update, name='record_update'),
    path('logout/', user_logout, name='logout'),
]
