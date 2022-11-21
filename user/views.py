from django.shortcuts import render
from rest_framework import viewsets
from user.models import User, Conta, Cartoes, Transacoes
from user.serializer import UserSerializer, ContaSerializer, CartoesSerializer, TransacoesSerializer
import pdb

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

    def create(self, request, *args, **kwargs):
      
        remetente = Conta.objects.get(pk = self.request.data['contaRemetente'])
        destinatario = Conta.objects.get(pk = self.request.data['contaDestinatario'])

       
        remetente.saldo -= self.request.data['valor']

        atualizarSaldoContaRemetente = {'agencia':remetente.agencia, 'conta': remetente.conta, 'user':remetente.user, 'saldo':remetente.saldo }
        atualizarSaldoContaDestinatario = {'agencia':destinatario.agencia, 'conta': destinatario.conta, 'user':destinatario.user, 'saldo':destinatario.saldo }
        print("aqui3")
        serializerRemetente = ContaSerializer(remetente, data = atualizarSaldoContaRemetente)
        serializerDestinatario = ContaSerializer(destinatario, data = atualizarSaldoContaDestinatario)
        if serializerRemetente.is_valid() and serializerDestinatario.is_valid():
            serializerDestinatario.save()
            serializerRemetente.save()
            return super().create(request, *args, **kwargs)
    
        
           

           