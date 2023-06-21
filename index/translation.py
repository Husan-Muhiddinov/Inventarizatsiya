from modeltranslation.translator import TranslationOptions, register

from index.models import Category, Responsible, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Responsible)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('fullname', 'description')

