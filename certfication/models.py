from django.db import models
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel, ActiveModel


class CompanyCertificate(BaseModel, ActiveModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    certificate = models.ImageField(upload_to="company_certificate/images/", verbose_name=_("certificate"))
    sub_title = models.CharField(max_length=200, verbose_name=_("sub_title"))
    text = models.TextField(verbose_name=_("text"))

    class Meta:
        db_table = "company_certificate"
        verbose_name = _("Company Certificate ")
        verbose_name_plural = _("6 Company Certificates")

    def __str__(self):
        return self.title
