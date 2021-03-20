from django.urls import path
from .views import OrderViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('', OrderViewSet)

urlpatterns = router.urls
