from django.urls import path
from user.views import UserViewSet, ContaViewSet, CartoesViewSet, TransacoesViewSet
from rest_framework import routers
router = routers.SimpleRouter()

router.register(r'user', UserViewSet),
router.register(r'conta', ContaViewSet),
router.register(r'cartao', CartoesViewSet),
router.register(r'transacao', TransacoesViewSet),

urlpatterns = router.urls