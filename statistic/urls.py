from django.urls import path
from statistic.views import StatisticListView


urlpatterns = [
    path("", StatisticListView.as_view(), name="statistic_list"),
]