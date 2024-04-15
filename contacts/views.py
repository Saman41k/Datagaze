from contacts.models import Contact
from contacts.serializers import ContactListSerializer
from rest_framework import generics


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
