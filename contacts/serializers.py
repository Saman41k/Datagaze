from rest_framework import serializers

from contacts.models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("icon", "contact")