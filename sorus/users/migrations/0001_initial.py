# Generated by Django 3.2 on 2021-06-04 02:23

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.state')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('notification_token', models.CharField(max_length=50)),
                ('profile_image', models.TextField(default='data:image/png;base64,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')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.state')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.usertype')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
