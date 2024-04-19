from django.db import models
from main.models import OrderModel
from django.utils.translation import gettext_lazy as _


class Partner(OrderModel):
    icon = models.ImageField(upload_to="statistic/icon/", verbose_name=_("icon"))
    url = models.URLField(max_length=200, verbose_name=_("Link"))

    class Meta:
        db_table = "partner"
        verbose_name = _("Partner ")
        verbose_name_plural = _("4 Partners")
        ordering = ("order",)
