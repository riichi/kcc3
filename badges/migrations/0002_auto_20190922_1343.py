# Generated by Django 2.2.5 on 2019-09-22 13:43

import badges.token_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='endpoint_url',
            field=models.URLField(blank=True, default='', verbose_name='Endpoint URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='badge',
            name='token',
            field=models.CharField(blank=True, default=badges.token_generator.generate_token, editable=False, max_length=64),
        ),
    ]
