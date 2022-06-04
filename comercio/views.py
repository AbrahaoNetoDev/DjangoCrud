from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello Word')


def article(request, year):
    return HttpResponse("O ano enviado foi: " + str(year))
