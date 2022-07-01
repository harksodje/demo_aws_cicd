# from django.contrib import admin
from django.urls import path

from .views import userlist

urlpatterns = [
    path('list', userlist.as_view(), name='list_user')
]
