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
        'foto': 'https://placehold.co/400x400/222/FFF?text=GOL',
        'nome': 'Carlos Rocha',
        'idade': 28,
        'posicao': 'Goleiro',
        'naturalidade': 'São Paulo, SP'
    },
    {
        'foto': 'https://placehold.co/400x400/333/FFF?text=ZAG',
        'nome': 'Bruno Alves',
        'idade': 31,
        'posicao': 'Zagueiro',
        'naturalidade': 'Rio de Janeiro, RJ'
    },
    {
        'foto': 'https://placehold.co/400x400/444/FFF?text=ZAG',
        'nome': 'Felipe Lima',
        'idade': 26,
        'posicao': 'Zagueiro',
        'naturalidade': 'Belo Horizonte, MG'
    },
    {
        'foto': 'https://placehold.co/400x400/555/FFF?text=LAT',
        'nome': 'Ricardo Gomes',
        'idade': 24,
        'posicao': 'Lateral Direito',
        'naturalidade': 'Porto Alegre, RS'
    },
    {
        'foto': 'https://placehold.co/400x400/666/FFF?text=LAT',
        'nome': 'Lucas Martins',
        'idade': 27,
        'posicao': 'Lateral Esquerdo',
        'naturalidade': 'Curitiba, PR'
    },
    {
        'foto': 'https://placehold.co/400x400/777/FFF?text=VOL',
        'nome': 'André Souza',
        'idade': 29,
        'posicao': 'Volante',
        'naturalidade': 'Salvador, BA'
    },
    {
        'foto': 'https://placehold.co/400x400/888/FFF?text=MEI',
        'nome': 'Gabriel Costa',
        'idade': 25,
        'posicao': 'Meio-campo',
        'naturalidade': 'Fortaleza, CE'
    },
    {
        'foto': 'https://placehold.co/400x400/999/FFF?text=MEI',
        'nome': 'Thiago Pereira',
        'idade': 22,
        'posicao': 'Meia Atacante',
        'naturalidade': 'Recife, PE'
    },
    {
        'foto': 'https://placehold.co/400x400/AAA/FFF?text=ATA',
        'nome': 'Matheus Oliveira',
        'idade': 30,
        'posicao': 'Atacante',
        'naturalidade': 'Manaus, AM'
    },
    {
        'foto': 'https://placehold.co/400x400/BBB/FFF?text=ATA',
        'nome': 'Pedro Henrique',
        'idade': 23,
        'posicao': 'Ponta Direita',
        'naturalidade': 'Goiânia, GO'
    },
    {
        'foto': 'https://placehold.co/400x400/CCC/FFF?text=ATA',
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
