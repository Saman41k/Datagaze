from rest_framework import serializers

from slider.models import First


class FirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = First
        fields = ('title', 'sub_title', 'image')