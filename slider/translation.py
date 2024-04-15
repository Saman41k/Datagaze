from modeltranslation.translator import register, TranslationOptions

from .models import First


@register(First)
class FirstTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )