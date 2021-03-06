# Generated by Django 3.0 on 2022-03-24 01:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import geoposition.fields
import reviews.models.photo_restaurant
import reviews.models.photo_review
import reviews.models.review
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('name', models.CharField(max_length=555, verbose_name='Name')),
                ('nit', models.CharField(max_length=20, verbose_name='NIT')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('location', geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name='Location')),
                ('website', models.CharField(blank=True, max_length=100, null=True, verbose_name='Web Site')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('category', models.TextField(blank=True, null=True, verbose_name='Category')),
                ('score', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score')),
                ('score_service', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Service')),
                ('score_food', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Food')),
                ('score_environment', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Environment')),
                ('score_quality_price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score Quality Price')),
                ('date_create', models.DateField(verbose_name='Date Create')),
                ('count_reviews', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Count Reviews')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopRestaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('top', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number Top')),
                ('score', models.IntegerField(blank=True, default=0, null=True, verbose_name='Score')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toprestaurant_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toprestaurant_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Top Restaurant',
                'verbose_name_plural': 'Top Restaurants',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('title', models.CharField(max_length=555, verbose_name='Title')),
                ('date', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='date')),
                ('description', models.TextField(verbose_name='Description')),
                ('score', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Score')),
                ('score_service', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=6, verbose_name='Score Service')),
                ('score_food', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=6, verbose_name='Score Food')),
                ('score_environment', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=6, verbose_name='Score Environment')),
                ('score_quality_price', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=6, verbose_name='Score Quality Price')),
                ('photo_one', models.ImageField(blank=True, null=True, upload_to=reviews.models.review.create_path_photo_review, verbose_name='Photo One')),
                ('photo_two', models.ImageField(blank=True, null=True, upload_to=reviews.models.review.create_path_photo_review, verbose_name='Photo Two')),
                ('photo_three', models.ImageField(blank=True, null=True, upload_to=reviews.models.review.create_path_photo_review, verbose_name='Photo Three')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='person')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Restaurant', verbose_name='restaurant')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhotoReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('photo_one', models.ImageField(blank=True, null=True, upload_to=reviews.models.photo_review.create_path_photo_review, verbose_name='Photo One')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photoreview_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photoreview_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review', verbose_name='Review')),
            ],
            options={
                'verbose_name': 'Photo Review',
                'verbose_name_plural': 'Photos Reviews',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhotoRestaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='date when the object was created', verbose_name='creation date')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='date when the object was modified', verbose_name='update date')),
                ('photo_one', models.ImageField(blank=True, null=True, upload_to=reviews.models.photo_restaurant.create_path_photo_restaurant, verbose_name='Photo One')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created the object', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photorestaurant_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creation user')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who performed the update', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photorestaurant_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='update user')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Photo Restaurant',
                'verbose_name_plural': 'Photos Restaurants',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
