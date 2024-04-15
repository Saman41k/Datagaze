from rest_framework import serializers
from partners.models import Partner


class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("icon", "url")