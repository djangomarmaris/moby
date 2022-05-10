from django.contrib import admin
from .models import Social ,Product ,About , Personel
# Register your models here.


class SocialAdmin(admin.ModelAdmin):
    list_display = ['add']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['author']

class PersonelAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Social,SocialAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Personel,PersonelAdmin)
