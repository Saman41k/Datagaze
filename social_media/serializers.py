from rest_framework import serializers
from social_media.models import SocialMedia


class SocialMediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("icon", "link")