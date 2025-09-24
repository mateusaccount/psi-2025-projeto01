from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('equipe/', views.pagina_equipe, name='equipe'),
    path('blog/', views.pagina_blog, name='blog'),
    path('sobre/', views.pagina_sobre, name='sobre'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]