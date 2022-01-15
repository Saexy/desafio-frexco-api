from django.contrib import admin
from django.urls import path, include
from frexco.views import RegionViewSet, FruitViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'regions', RegionViewSet)
router.register(r'fruits', FruitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
