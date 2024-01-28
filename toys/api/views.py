from rest_framework import viewsets
from rest_framework.response import Response
from .models import Toys
from .serializers import ToySerializer
class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toys.objects.all()
    serializer_class = ToySerializer
    def retrieve(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = self.get_serializer(instance)
       return Response(serializer.data)