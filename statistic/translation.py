from modeltranslation.translator import register, TranslationOptions

from .models import Statistic


@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )