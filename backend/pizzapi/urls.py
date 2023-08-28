from django.urls import path, include
from .views import getCommands, getPizzas

urlpatterns = [
    path('', getCommands),
    path('pizza/', getPizzas),
]

