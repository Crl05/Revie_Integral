# Generated by Django 3.0 on 2022-03-21 14:27

from django.db import migrations, models
import django.utils.timezone
import users.managers.person_manager
import users.models.person


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('rol', models.CharField(blank=True, help_text='Reviewer = RW, Restaurant = RT, Admin = AD', max_length=10, null=True, verbose_name='Rol')),
                ('first_name', models.CharField(max_length=555, verbose_name='Name')),
                ('last_name', models.CharField(max_length=555, verbose_name='Last Name')),
                ('age', models.IntegerField(default='0', verbose_name='Age')),
                ('gender', models.CharField(max_length=3, verbose_name='Gender')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=users.models.person.create_path_reviewer, verbose_name='Photo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
            managers=[
                ('objects', users.managers.person_manager.PersonManager()),
            ],
        ),
    ]
