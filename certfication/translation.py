from modeltranslation.translator import register, TranslationOptions

from .models import CompanyCertificate


@register(CompanyCertificate)
class CompanyCertificateTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )