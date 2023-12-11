# imports
from django.urls import path
from . import views


urlpatterns = [
    path('', views.DDA, name='DDA'),
    path('bresenham', views.bresenham, name='bresenham'),
    path('DDA', views.DDA, name='DDA'),
    path('midpoint', views.midpoint_circle , name='midpoint'),
    path('location', views.geocode_address , name='location'),

        ]
