from django.shortcuts import render
from rest_framework import viewsets
from farmer.models import Auth_Token
from .serializers import Auth_TokenSerializer

# Create your views here.
class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Auth_Token.objects.all()
    serializer_class = Auth_TokenSerializer