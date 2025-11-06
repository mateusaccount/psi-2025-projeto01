from django.shortcuts import render, get_object_or_404
from .models import Post

info_site = {
    'titulo_site': 'Vasco da Gama',
    'ano_copyright': 2025,
    'autores': [
        'Mateus Cosme',
    ],
    'descricao_site': 'Este é um site de demonstração criado com Django para apresentar a equipe do Vasco da Gama. Todos os dados são reais.'
}

dados_equipe = [
    {
        'foto': 'images/LeoJardim.png',
        'nome': 'Leo Jardim',
        'idade': 30,
        'posicao': 'Goleiro',
        'naturalidade': 'Ribeirão Preto, São Paulo'
    },
    {
        'foto': 'images/Cuesta.png',
        'nome': 'Carlos Cuesta',
        'idade': 26,
        'posicao': 'Zagueiro',
        'naturalidade': 'Quibdó, Colombia'
    },
    {
        'foto': 'images/RobertRenan.png',
        'nome': 'Robert Renan',
        'idade': 21,
        'posicao': 'Zagueiro',
        'naturalidade': 'Brasília, Distrito Federal'
    },
    {
        'foto': 'images/PH.png',
        'nome': 'Paulo Henrique',
        'idade': 29,
        'posicao': 'Lateral Direito',
        'naturalidade': 'Sete Barras, São Paulo'
    },
    {
        'foto': 'images/LucasPiton.png',
        'nome': 'Lucas Piton',
        'idade': 24,
        'posicao': 'Lateral Esquerdo',
        'naturalidade': 'Jundiaí, São Paulo'
    },
    {
        'foto': 'images/TcheTche.png',
        'nome': 'Tchê Tchê',
        'idade': 33,
        'posicao': 'Volante',
        'naturalidade': 'São Paulo, São Paulo'
    },
    {
        'foto': 'images/Coutinho.png',
        'nome': 'Philippe Coutinho',
        'idade': 33,
        'posicao': 'Meio-campo',
        'naturalidade': 'Rio de Janeiro, Rio de Janeiro'
    },
    {
        'foto': 'images/AndresGomez.png',
        'nome': 'Andrés Gómez',
        'idade': 23,
        'posicao': 'Meia Atacante',
        'naturalidade': 'Quibdó, Colômbia'
    },
    {
        'foto': 'images/Dvd.png',
        'nome': 'David Corrêa',
        'idade': 29,
        'posicao': 'Atacante',
        'naturalidade': 'Vitória, Espírito Santo'
    },
    {
        'foto': 'images/NunoMoreira.png',
        'nome': 'Nuno Moreira',
        'idade': 26,
        'posicao': 'Ponta Direita',
        'naturalidade': 'Espinho, Portugal'
    },
    {
        'foto': 'images/Vegetti.png',
        'nome': 'Pablo Vegetti',
        'idade': 36,
        'posicao': 'Centroavante',
        'naturalidade': 'Santo Domingo, Argentina'
    }
]

def pagina_inicio(request):
    context = {}
    context.update(info_site)
    return render(request, 'inicio.html', context)

def pagina_equipe(request):
    context = {
        'equipe': dados_equipe,
    }
    context.update(info_site)
    return render(request, 'equipe.html', context)

def pagina_blog(request):
    """
    View para listar todos os posts do blog.
    """
    # Busca todos os posts no banco, ordenados do mais novo para o mais antigo
    posts = Post.objects.all().order_by('-data_publicacao')
    
    context = {
        'posts': posts
    }
    context.update(info_site)
    return render(request, 'blog.html', context) # Caminho corrigido

def pagina_sobre(request):
    context = {}
    context.update(info_site)
    return render(request, 'sobre.html', context)

# A view 'post_list' foi REMOVIDA daqui, pois sua lógica foi unificada na 'pagina_blog'.

def post_detail(request, pk):
    """
    View para exibir os detalhes de uma única postagem.
    """
    # Busca o post pelo ID (pk) ou retorna um erro 404 se não existir
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post
    }
    context.update(info_site) # Adicionado para o base.html funcionar
    return render(request, 'post.html', context) # Caminho corrigido