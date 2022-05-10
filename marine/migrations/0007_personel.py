# Generated by Django 4.0.2 on 2022-04-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marine', '0006_remove_about_staff_remove_about_staff2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('name', models.CharField(db_index=True, default='mobymarine', max_length=200, verbose_name='Name')),
                ('contact', models.CharField(db_index=True, default='mobymarine@xxx.com', max_length=200, verbose_name='Phone or EMail')),
            ],
        ),
    ]