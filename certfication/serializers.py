from rest_framework import serializers
from certfication.models import CompanyCertificate


class CompanyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCertificate
        fields = ("certificate", "title", "sub_title", "text")