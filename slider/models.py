from django.db import models
from django.utils.translation import gettext_lazy as _
from main.models import OrderModel


class First(OrderModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    sub_title = models.CharField(max_length=200, verbose_name=_('description'))
    image = models.ImageField(upload_to="slider/image/", verbose_name=_("image"))

    class Meta:
        db_table = "slider"
        verbose_name = _("Slider ")
        verbose_name_plural = _("2 Sliders")
        ordering = ("order",)

    def __str__(self):
        return self.title