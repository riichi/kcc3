# Generated by Django 2.2.5 on 2019-09-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='usma_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]