from django.db import models
from main.models import OrderModel
from django.utils.translation import gettext_lazy as _


class Contact(OrderModel):
    icon = models.ImageField(upload_to="contact/icons/", verbose_name=_("icon"))
    contact = models.CharField(max_length=255, verbose_name=_("contact"))

    class Meta:
        db_table = "contact"
        verbose_name = _("Contact ")
        verbose_name_plural = _("9 Contacts")
        ordering = ("order",)
