from rest_framework import generics
from .models import Model1
from .serializers import Model1Serializer

class Model1Lista(generics.ListCreateAPIView):
    queryset = Model1.objects.all()
    serializer_class = Model1Serializer

class Model1Szczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model1.objects.all()
    serializer_class = Model1Serializer