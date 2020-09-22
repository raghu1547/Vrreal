from django.urls import path,re_path
from .views import search

app_name = 'build'

urlpatterns = [
    path('list/',search,name='list'),

]