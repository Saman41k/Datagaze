from rest_framework.views import APIView, Response
from certfication.models import CompanyCertificate
from certfication.serializers import CompanyCertificateSerializer


class CompanyCertificateView(APIView):
    def get(self, obj):
        queryset = CompanyCertificate.objects.filter(active=True).first()
        serializer = CompanyCertificateSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)
