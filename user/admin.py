from django.contrib import admin
from user.models import User, Conta, Cartoes, Transacoes
# Register your models here.
admin.site.register(User)
admin.site.register(Conta)
admin.site.register(Cartoes)
admin.site.register(Transacoes)