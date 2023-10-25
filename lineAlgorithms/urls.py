# imports
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('brensenham', views.brensenham, name='brensenham'),
    path('DDA', views.DDA, name='DDA'),
    


        ]
