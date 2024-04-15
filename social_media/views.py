from social_media.models import SocialMedia
from social_media.serializers import SocialMediaListSerializer
from rest_framework import generics


class SocialMediaListView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaListSerializer
