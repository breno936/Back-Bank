from django.shortcuts import render
from rest_framework import viewsets
from user.models import User, Conta, Cartoes, Transacoes
from user.serializer import UserSerializer, ContaSerializer, CartoesSerializer, TransacoesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartoesViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartoesSerializer

class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer