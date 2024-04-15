from django.db import models
from main.models import OrderModel
from django.utils.translation import gettext_lazy as _


class SocialMedia(OrderModel):
    icon = models.ImageField(upload_to="social_media/icons/", verbose_name=_("icon"))
    link = models.URLField(max_length=255, verbose_name=_("link"))

    class Meta:
        db_table = "social_media"
        verbose_name = _("SocialMedia ")
        verbose_name_plural = _("8 SocialMedias")
        ordering = ("order",)
