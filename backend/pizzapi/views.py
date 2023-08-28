from django.http import JsonResponse
from .models import Pizza, Topping

# Create your views here.

def getCommands(request):
    endpoints = {
        'api/pizzas' : "Return all pizzas"
    }

    return JsonResponse (endpoints)

def getPizzas(request):

    pizzas = Pizza.objects.all()

    serialized_pizzas = []

    for pizza in pizzas:
        serialized_pizzas.append(pizza.serializer())

    return JsonResponse(serialized_pizzas, safe=False)