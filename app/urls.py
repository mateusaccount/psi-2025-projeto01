from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('equipe/', views.pagina_equipe, name='equipe'),
    path('sobre/', views.pagina_sobre, name='sobre'),
]