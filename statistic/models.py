from django.db import models
from django.utils.translation import gettext_lazy as _
from main.models import OrderModel, ActiveModel


class Statistic(OrderModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    icon = models.ImageField(upload_to="statistic/icon/", verbose_name=_("icon"))

    class Meta:
        db_table = "statistic"
        verbose_name = _("Statistic ")
        verbose_name_plural = _("3 Statistics")
        ordering = ("order",)

    def __str__(self):
        return self.title