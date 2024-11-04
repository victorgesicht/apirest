from django.shortcuts import render
from rest_framework import generics
from .models import todo
from .serializers import todoSerializer


class todoListCreate(generics.ListCreateAPIView):
    queryset=todo.objects.all()
    serializer_class=todoSerializer

class todoListCreateRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset=todo.objects.all()
    serializer_class=todoSerializer
    lookup_field="pk"
