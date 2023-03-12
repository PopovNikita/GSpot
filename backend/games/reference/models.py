from django.db import models
import uuid

from core.models import Product


class Language(models.Model):
    id = models.UUIDField('UUID языка',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField('Наименование языка',
                            max_length=100,
                            help_text='Введите наименование языка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class ProductLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                 related_name='game_supported_language')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='languages')
    interface = models.BooleanField(verbose_name='Интерфейс', default=True)
    subtitles = models.BooleanField(verbose_name='Титры', default=True)
    voice = models.BooleanField(verbose_name='Озвучка', default=True)

    def __str__(self):
        return self.language.name + "|" + self.product.name

    class Meta:
        verbose_name = 'Поддерживаемый язык'
        verbose_name_plural = 'Поддерживаемые языки'
