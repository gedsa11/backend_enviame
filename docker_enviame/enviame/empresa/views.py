from django.shortcuts import render
from .models import Empresa
from rest_framework import viewsets
from .serializers import EmpresaSerializer

# Create your views here.
class EmpresaViewset(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer