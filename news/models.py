from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import BaseModel, ActiveModel


class News(BaseModel, ActiveModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    sub_title = models.CharField(max_length=200, verbose_name=_("sub title"))
    cover = models.ImageField(upload_to="news/cover/")
    slug = models.SlugField(max_length=200, verbose_name=_("slug"))
    text = models.TextField(verbose_name=_("text"))

    class Meta:
        db_table = "news"
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class StaticPage(BaseModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub title"))
    text = models.TextField(verbose_name=_("text"))

    class Meta:
        db_table = "static_page"
        verbose_name = _("Static Page ")
        verbose_name_plural = _("Static Pages")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

