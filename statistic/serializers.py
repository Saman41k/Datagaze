from rest_framework import serializers
from statistic.models import Statistic


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ("title", "icon")