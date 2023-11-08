from modeltranslation.translator import translator, TranslationOptions

from core.models import *



class ProductTranslationOptions(TranslationOptions):
    fields=('title','content',)


class BlogTranslationOptions(TranslationOptions):
    fields=('title','content',)

class SettingTranslationOptions(TranslationOptions):
    fields=('title', 'description')


class TestimonialTranslationOptions(TranslationOptions):
    fields=('name', 'content', 'position')


translator.register(Testimonial,TestimonialTranslationOptions)
translator.register(Blog,BlogTranslationOptions)
translator.register(Product,ProductTranslationOptions)
translator.register(Setting,SettingTranslationOptions)
