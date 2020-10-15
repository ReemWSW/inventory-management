
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detial', views.detial, name='detial'),
    path('insert', views.insert, name='insert'),
]
