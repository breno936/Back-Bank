from rest_framework import serializers
from user.models import User, Conta, Cartoes, Transacoes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'data_nasc', 'hash_password', 'salt_password']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['agencia', 'conta', 'saldo', 'user_id']

class CartoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoes
        fields = ['id', 'senha', 'limite', 'conta_id']

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = ['id', 'valor', 'contaDestinatario', 'contaRemetente']
