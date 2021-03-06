# Generated by Django 4.0.2 on 2022-04-20 18:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(db_index=True, max_length=200)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('staff', models.ImageField(blank=True, upload_to='images/')),
                ('staff_number', models.CharField(db_index=True, max_length=200)),
                ('staff2', models.ImageField(blank=True, upload_to='images/')),
                ('staff_number2', models.CharField(db_index=True, max_length=200)),
                ('staff3', models.ImageField(blank=True, upload_to='images/')),
                ('staff_number3', models.CharField(db_index=True, max_length=200)),
                ('aboutUs', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
