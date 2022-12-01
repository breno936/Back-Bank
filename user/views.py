import decimal
from http.client import HTTPResponse
import random
from django.shortcuts import render
from rest_framework import viewsets
from user.models import User, Conta, Cartoes, Transacoes
from user.serializer import UserSerializer, ContaSerializer, CartoesSerializer, TransacoesSerializer
import pdb
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_login = User.objects.filter(name = self.request.data['name'])
        print(user_login)
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        usuario_criado = User.objects.last()
        # print(usuario_criado.id)
        # agencia = random.randint(1000, 8000)
        # conta = random.randint(10000000, 80000000)
        # novaConta = {'agencia':agencia, 'conta':conta, 'user':7, 'saldo':decimal.Decimal(1000)}
        # serializerConta = ContaSerializer(data=novaConta)
        # if serializerConta.is_valid():
        #     serializerConta.instance.
        #     serializerConta.save()
        return Response(status=status.HTTP_200_OK)

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartoesViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartoesSerializer

class TransacoesViewSet(viewsets.ModelViewSet):

    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer

    def create(self, request, *args, **kwargs):
        print("aqui")
        remetente = Conta.objects.get(pk = self.request.data['contaRemetente'])
        destinatario = Conta.objects.get(pk = self.request.data['contaDestinatario'])

        if remetente.saldo >= self.request.data['valor']:
            remetente.saldo -= decimal.Decimal(self.request.data['valor'])
            destinatario.saldo += decimal.Decimal(self.request.data['valor'])

            atualizarSaldoContaRemetente = {'agencia':remetente.agencia, 'conta': remetente.conta, 'user':remetente.user, 'saldo':remetente.saldo }
            atualizarSaldoContaDestinatario = {'agencia':destinatario.agencia, 'conta': destinatario.conta, 'user':destinatario.user, 'saldo':destinatario.saldo }
            print("aqui3")
            serializerRemetente = ContaSerializer(remetente, data = atualizarSaldoContaRemetente)
            serializerDestinatario = ContaSerializer(destinatario, data = atualizarSaldoContaDestinatario)
            if serializerRemetente.is_valid() and serializerDestinatario.is_valid():
                serializerDestinatario.save()
                serializerRemetente.save()
                return super().create(request, *args, **kwargs)
    
        
           

           