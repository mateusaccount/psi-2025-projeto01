from django.shortcuts import render

info_site = {
    'titulo_site': 'Vasco da Gama',
    'ano_copyright': 2024,
    'autores': [
        'Mateus Cosme',
    ],
    'descricao_site': 'Este é um site de demonstração criado com Django para apresentar uma equipe esportiva fictícia. Todos os dados são fictícios.'
}

dados_equipe = [
    {
        'foto': 'images/LeoJardim.png',
        'nome': 'Leo Jardim',
        'idade': 30,
        'posicao': 'Goleiro',
        'naturalidade': 'Ribeirão Preto, SP'
    },
    {
        'foto': 'images/Cuesta.png',
        'nome': 'Bruno Alves',
        'idade': 31,
        'posicao': 'Zagueiro',
        'naturalidade': 'Rio de Janeiro, RJ'
    },
    {
        'foto': 'images/RobertRenan.png',
        'nome': 'Felipe Lima',
        'idade': 26,
        'posicao': 'Zagueiro',
        'naturalidade': 'Belo Horizonte, MG'
    },
    {
        'foto': 'images/PH.png',
        'nome': 'Ricardo Gomes',
        'idade': 24,
        'posicao': 'Lateral Direito',
        'naturalidade': 'Porto Alegre, RS'
    },
    {
        'foto': 'images/LucasPiton.png',
        'nome': 'Lucas Martins',
        'idade': 27,
        'posicao': 'Lateral Esquerdo',
        'naturalidade': 'Curitiba, PR'
    },
    {
        'foto': 'images/TcheTche.png',
        'nome': 'André Souza',
        'idade': 29,
        'posicao': 'Volante',
        'naturalidade': 'Salvador, BA'
    },
    {
        'foto': 'images/Coutinho.png',
        'nome': 'Gabriel Costa',
        'idade': 25,
        'posicao': 'Meio-campo',
        'naturalidade': 'Fortaleza, CE'
    },
    {
        'foto': 'images/AndresGomez.png',
        'nome': 'Thiago Pereira',
        'idade': 22,
        'posicao': 'Meia Atacante',
        'naturalidade': 'Recife, PE'
    },
    {
        'foto': 'images/Dvd.png',
        'nome': 'Matheus Oliveira',
        'idade': 30,
        'posicao': 'Atacante',
        'naturalidade': 'Manaus, AM'
    },
    {
        'foto': 'images/NunoMendes.png',
        'nome': 'Pedro Henrique',
        'idade': 23,
        'posicao': 'Ponta Direita',
        'naturalidade': 'Goiânia, GO'
    },
    {
        'foto': 'images/Vegetti.png',
        'nome': 'Rafael Santos',
        'idade': 28,
        'posicao': 'Centroavante',
        'naturalidade': 'Florianópolis, SC'
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

# View para a página sobre
def pagina_sobre(request):
    context = {}
    context.update(info_site)
    return render(request, 'sobre.html', context)
