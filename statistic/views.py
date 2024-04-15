from rest_framework import generics
from statistic.models import Statistic
from statistic.serializers import StatisticListSerializer


class StatisticListView(generics.ListAPIView):
    queryset = Statistic.objects.filter(active=True)
    serializer_class = StatisticListSerializer