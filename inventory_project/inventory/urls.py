
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_item', views.list_item, name='list_item'),
    path('add_item', views.add_item, name='add_item'),
    path('update_item/<str:pk>', views.update_item, name='update_item'),
    path('delete_item/<str:pk>', views.delete_item, name='delete_item'),
]
