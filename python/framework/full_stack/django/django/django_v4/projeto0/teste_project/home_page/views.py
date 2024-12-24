from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Olá Mundo. Index Views')


def aqui(request):
    return HttpResponse('Agora estou na pag, Aqui')
