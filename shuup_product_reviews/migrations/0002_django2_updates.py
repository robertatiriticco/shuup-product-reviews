# Generated by Django 2.2.15 on 2020-08-07 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_product_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productreview',
            unique_together=set(),
        ),
    ]
