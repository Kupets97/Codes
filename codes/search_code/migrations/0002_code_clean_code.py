# Generated by Django 4.1.5 on 2023-04-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_code', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='clean_code',
            field=models.CharField(blank=True, db_index=True, max_length=10, null=True, unique=True, verbose_name='Clean Code'),
        ),
    ]