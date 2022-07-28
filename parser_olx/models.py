#from unicodedata import category
from django.db import models

class Category (models.Model):
    link_to_category_page = models.CharField(max_length=255,verbose_name="Посилання на сторінку")
    date_of_last_update = models.DateTimeField( auto_now=True, verbose_name="Дата оновлення")
    #data_string = models.TextField(verbose_name="Конвертовані дані", blank=True, null=True)

    class Meta:
        verbose_name = ("Категорія")
        verbose_name_plural = ("Категорії")
    def __str__ (self):
        return '{}  ({})'.format (self.link_to_category_page, self.date_of_last_update) 

class Product (models.Model):
    category = models.ForeignKey(Category, related_name='kategory_product', on_delete=models.CASCADE, verbose_name="Пов'язана категорія")
    link_to_product = models.CharField(max_length=255,verbose_name="Посилання на сторінку")
    title = models.CharField(max_length=100,verbose_name="Назва", blank=True, null=True)
    price = models.CharField(max_length=20, verbose_name="Ціна", blank=True, null=True)
    locacion = models.CharField(max_length=100,verbose_name="Локація", blank=True, null=True)
    date_of_creating =  models.CharField(max_length=100,verbose_name="Дата створення", blank=True, null=True)
    photo_link = models.CharField(max_length=255,verbose_name="Посилання на фото", blank=True, null=True)
    description = models.TextField(verbose_name="Конвертовані дані", blank=True, null=True)

    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ("Товари")
    def __str__ (self):
        return '{}  ({})'.format (self.title, self.locacion) 