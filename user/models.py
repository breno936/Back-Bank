from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    data_nasc = models.DateField()
    hash_password = models.CharField(max_length=200)
    salt_password = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Conta(models.Model):
    agencia = models.IntegerField()
    conta = models.CharField(max_length=200, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.conta

class Transacoes(models.Model):
    contaRemetente = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name="contaRemetente")
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    contaDestinatario = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name="contaDestinatario")

    def __str__(self) -> str:
        return str(self.id)

class Cartoes(models.Model):
    DEBITO = "DE"
    CREDITO = "CR"
    TIPOS_CARTOES = [
        (DEBITO, "Débito"),
        (CREDITO, "Crédito"),
    ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    tipo = TIPOS_CARTOES
    senha = models.IntegerField()
    limite = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.tipo
