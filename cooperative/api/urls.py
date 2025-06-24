from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet



router = DefaultRouter()
router.register(r"farmer", FarmerViewSet, basename = "farmer")

urlpatterns = [
    path("", include(router.urls)),

]