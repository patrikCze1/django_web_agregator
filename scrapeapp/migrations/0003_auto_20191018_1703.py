# Generated by Django 2.2.6 on 2019-10-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapeapp', '0002_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
