# Generated by Django 3.1.5 on 2021-08-16 19:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LifeStyleCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NewsSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PressReleaseForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator])),
                ('logo', models.ImageField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('discount_description', models.TextField()),
                ('release_date', models.DateField()),
                ('sample', models.FileField(upload_to='')),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('schedule_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_content', models.TextField()),
                ('post_title', models.CharField(max_length=1000)),
                ('post_status', models.CharField(max_length=100)),
                ('post_modified', models.DateTimeField(auto_now=True, null=True)),
                ('tags', models.CharField(max_length=500, null=True)),
                ('keywords', models.CharField(max_length=500, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('meta_title', models.CharField(max_length=500)),
                ('meta_description', models.TextField(null=True)),
                ('feature_image_url', models.ImageField(max_length=1000, upload_to='')),
                ('seen', models.BigIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_id', to='blog.category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_id', to='blog.lifestylecities')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
