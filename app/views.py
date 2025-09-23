from django.shortcuts import render

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

def pagina_sobre(request):
    context = {}
    context.update(info_site)
    return render(request, 'sobre.html', context)
