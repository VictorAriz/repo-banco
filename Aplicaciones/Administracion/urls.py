from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarTurno/', views.registrarTurno)
    
    
]


urlpatterns = [
    path('', views.home2),
    path('registrarTurno/', views.registrarTurno),
    path('turnosListados/', views.home)
]

