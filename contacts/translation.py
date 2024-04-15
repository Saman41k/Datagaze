from modeltranslation.translator import register, TranslationOptions

from .models import Contact


@register(Contact)
class ContactTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )