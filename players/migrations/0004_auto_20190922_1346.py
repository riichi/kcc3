# Generated by Django 2.2.5 on 2019-09-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20190920_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='discord_id',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Discord ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='usma_id',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='USMA ID'),
            preserve_default=False,
        ),
    ]