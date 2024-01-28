from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToyViewSet
router = DefaultRouter()
router.register('toys',ToyViewSet)
urlpatterns = [
    path('',include(router.urls))
]