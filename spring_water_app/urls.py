from django.urls import path
from spring_water_app import views

urlpatterns = [
    path('', views.index, name='index'),
]