from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello Word')


def article(request, year):
    return HttpResponse("O ano enviado foi: " + str(year))


def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'nome', 'idade': 0}


def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse(result['nome'] + ' tem ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse(result['nome'] + ' não encontrado')

