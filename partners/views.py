from partners.models import Partner
from partners.serializers import PartnerListSerializer
from rest_framework import generics


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerListSerializer
