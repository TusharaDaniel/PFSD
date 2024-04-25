from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('viewposts', views.viewposts, name='viewposts')

]