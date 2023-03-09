from django.urls import path 
from . import views

urlpatterns = [
    path('', views.create_item, name='index'),  
    path('delete/<str:id>', views.delete_item, name='delete'),
]