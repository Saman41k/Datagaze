from django.urls import path

from .views import FirstListView

urlpatterns = [
    path("", FirstListView.as_view(), name="slider_list"),
]