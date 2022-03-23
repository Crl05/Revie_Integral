# Generated by Django 3.0 on 2022-03-23 00:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220322_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='score_environment',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Environment'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='score_food',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Food'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='score_quality_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Quality Price'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='score_service',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Service'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(blank=True, default=0, max_length=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score'),
        ),
    ]