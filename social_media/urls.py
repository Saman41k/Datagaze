from django.urls import path
from social_media.views import SocialMediaListView


urlpatterns = [
    path("", SocialMediaListView.as_view(), name="social_media_list"),
]