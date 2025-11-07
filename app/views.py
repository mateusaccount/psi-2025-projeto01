from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Post, Jogador
from .forms import JogadorForm

info_site = {
    'titulo_site': 'Vasco da Gama',
    'ano_copyright': 2025,
    'autores': [
        'Mateus Cosme',
    ],
    'descricao_site': 'Este é um site de demonstração criado com Django para apresentar a equipe do Vasco da Gama. Todos os dados são reais.'
}

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_superuser, login_url='/admin/login/')(view_func)

def pagina_inicio(request):
    context = {}
    context.update(info_site)
    return render(request, 'inicio.html', context)

def pagina_sobre(request):
    context = {}
    context.update(info_site)
    return render(request, 'sobre.html', context)

def pagina_equipe(request):
    jogadores_do_banco = Jogador.objects.all().order_by('nome') 
    
    context = {
        'equipe': jogadores_do_banco,
    }
    context.update(info_site)
    return render(request, 'equipe.html', context)

def pagina_blog(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    
    context = {
        'posts': posts
    }
    context.update(info_site)
    return render(request, 'blog.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post
    }
    context.update(info_site)
    return render(request, 'post.html', context)

@superuser_required
def jogador_novo(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = JogadorForm()
        
    context = {
        'form': form,
        'titulo_pagina': 'Adicionar Novo Jogador'
    }
    context.update(info_site)
    return render(request, 'jogador_form.html', context)

@superuser_required # 3. Segurança!
def jogador_editar(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = JogadorForm(instance=jogador)
        
    context = {
        'form': form,
        'titulo_pagina': f'Editando: {jogador.nome}'
    }
    context.update(info_site)
    return render(request, 'jogador_form.html', context)

@superuser_required
def jogador_excluir(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    
    if request.method == 'POST':
        jogador.delete()
        return redirect('equipe')
    
    context = {'jogador': jogador}
    context.update(info_site)
    return render(request, 'jogador_confirm_delete.html', context)