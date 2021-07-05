from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('map1', views.map1, name='map1'),
    path('map2', views.map2, name='map2'),
    path('map3', views.map3, name='map3'),
    path('map4', views.map4, name='map4'),

]
