from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group


Group.add_to_class('max_limit_product', models.BigIntegerField(null=True, default=300, verbose_name=_('Max limit product')))
Group.add_to_class('max_limit_responsible', models.BigIntegerField(null=True, default=50, verbose_name=_('Max limit responsible')))
Group.add_to_class('max_limit_category', models.BigIntegerField(null=True, default=30, verbose_name=_('Max limit category')))
Group.add_to_class('max_limit_model', models.BigIntegerField(null=True, default=30, verbose_name=_('Max limit model')))
Group.add_to_class('ui', models.BooleanField(null=True, default=False, verbose_name=_('Building UI design')))

class RoomsModel(models.Model):
    rooms = models.CharField(max_length=10, verbose_name=_('rooms'))
    floor = models.CharField(max_length=10, verbose_name=_('floor'))

    def __str__(self):
        return self.rooms

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Category(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name


class Responsible(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100, verbose_name=_('fullname'))
    description = models.TextField(verbose_name=_('description'))

    def __str__(self) -> str:
        return self.fullname


class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, verbose_name=_('name'), null=True, blank=True)
    schet = models.CharField(max_length=255, verbose_name=_('schet'), null=True, blank=True)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, blank=True, verbose_name=_('category_id'), null=True)
    room_number = models.CharField(max_length=30, verbose_name=_('room_number'), blank=True, null=True)
    inventar_number = models.CharField(max_length=255, unique=True, blank=True, verbose_name=_('inventar_number'))
    model_id = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, verbose_name=_('model_id'), null=True)
    responsible_id = models.ForeignKey(Responsible, on_delete=models.SET_NULL, verbose_name=_('responsible_id'), blank=True, null=True)
    seria_number = models.CharField(max_length=70, blank=True, null=True, verbose_name=_('seria_number'))
    images = models.ImageField(upload_to='person', verbose_name=_('images'), blank=True)
    status = models.IntegerField(null=True, default=1, verbose_name='status')
    description = models.TextField(verbose_name=_('description'), blank=True)
    year_of_manufacture = models.CharField(max_length=50, verbose_name=_('year_of_manufacture'), blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=50, verbose_name=_('unit_of_measurement'), blank=True, null=True)
    qr_code = models.ImageField(blank=True, upload_to='images/code', verbose_name=_('qr_code'))
    responsible_person = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('responsible_person'))
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('updated_at'))

    def __str__(self) -> str:
        return str(self.inventar_number)

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(
            f"Inventar raqami: {self.inventar_number} \n Javobgar shaxs: {'Nomalum' if self.responsible_id is None else self.responsible_id.fullname } \n Xona: {self.room_number} \n ")
        qr_offset = Image.new('RGB', (570, 570), 'white')
        qr_offset.paste(qr_image)
        files_name = f'{self.inventar_number}---qrcode.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
