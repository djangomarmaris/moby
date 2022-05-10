from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Social(models.Model):
    add = models.CharField(max_length=20, db_index=True,verbose_name='Ekleyen',default='İsim Giriniz.')
    fb = models.CharField(max_length=20, db_index=True)
    insta = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.add




class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return self.name



class About(models.Model):
    author = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    aboutUs = RichTextUploadingField()

    def __str__(self):
        return self.author


class Personel(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    name = models.CharField(max_length=200, db_index=True ,verbose_name='Name',default='mobymarine')
    contact = models.CharField(max_length=200, db_index=True,verbose_name='Phone or EMail',default='mobymarine@xxx.com')


    def __str__(self):
        return self.name