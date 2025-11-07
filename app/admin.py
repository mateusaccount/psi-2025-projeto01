from django.contrib import admin
from .models import Post, Jogador

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo', 'texto')
    list_filter = ('data_publicacao',)

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'posicao', 'idade')
    search_fields = ('nome', 'posicao')
    list_filter = ('posicao',)