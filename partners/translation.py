from modeltranslation.translator import register, TranslationOptions

from .models import Partner


@register(Partner)
class PartnerTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )