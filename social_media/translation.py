from modeltranslation.translator import register, TranslationOptions

from .models import SocialMedia


@register(SocialMedia)
class SocialMediaTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )