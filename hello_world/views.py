from django.shortcuts import render
from django.http import HttpResponse
# What django.http does?
# recebe a requisição HTTP (GET, POST, etc.) do navegador do usuário.
# Ele pega todos os dados dessa requisição (cabeçalhos, dados de formulário, cookies, etc.) e os empacota em um objeto Python chamado HttpRequest
# O URL Dispatcher (urls.py) pega este objeto HttpRequest e o passa como o argumento request para a sua função index: def index(request)
# O Django fez todo o trabalho de parsing! Você só precisa usar o objeto request se precisar de dados dele.
# Para que o Django saiba como empacotar sua resposta para o navegador, você usa o objeto HttpResponse importado de django.http.

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")
