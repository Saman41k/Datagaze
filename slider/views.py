from rest_framework import generics

from slider.models import First
from slider.serializers import FirstSerializer


class FirstListView(generics.ListAPIView):
    queryset = First.objects.all()
    serializer_class = FirstSerializer
