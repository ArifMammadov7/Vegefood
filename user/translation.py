from modeltranslation.translator import translator,TranslationOptions

from core.models import Setting,Product

class SettingTranslationOptions(TranslationOptions):
    fields=('title',)

class ProductTranslationOptions(TranslationOptions):
    fields=('title','content',)