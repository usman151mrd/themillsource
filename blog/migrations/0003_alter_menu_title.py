# Generated by Django 3.2.8 on 2021-10-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211030_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
