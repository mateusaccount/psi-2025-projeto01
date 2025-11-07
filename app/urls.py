from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('equipe/', views.pagina_equipe, name='equipe'),
    path('sobre/', views.pagina_sobre, name='sobre'),
    path('blog/', views.pagina_blog, name='blog'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('jogador/novo/', views.jogador_novo, name='jogador_novo'),
    path('jogador/<int:pk>/editar/', views.jogador_editar, name='jogador_editar'), 
    path('jogador/<int:pk>/excluir/', views.jogador_excluir, name='jogador_excluir'),
]