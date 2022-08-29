from django.urls import path, include
from app import views
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('login/', login, name="login"),
    path('emp', emp, name="emp"),  
    path('show', show),
    path('index', index),
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy),
    path('new_post', new_post, name="new_post"),
    path('show_post', show_post, name="show_post"),
    path('edit_post/<int:id>', edit_post),
    path('update_post/<int:id>', update_post),
    path('destroy_post/<int:id>', destroy_post),
]
