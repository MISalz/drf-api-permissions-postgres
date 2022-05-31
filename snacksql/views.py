from rest_framework import generics
from .serializers import SnacksSerializer
from .models import SnackSQL
from .permissions import IsOwnerOrReadOnly

# Create your views here.

# class SnackList(generics.ListAPIView):
#   queryset= Snack.objects.all()
#   serializer_class= SnacksSerializer  

class SnackList(generics.ListCreateAPIView):
  queryset = SnackSQL.objects.all()
  serializer_class = SnacksSerializer  

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = SnackSQL.objects.all()
  serializer_class = SnacksSerializer  
  permission_classes = (IsOwnerOrReadOnly)

