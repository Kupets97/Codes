# Generated by Django 4.1.5 on 2023-01-19 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='Код')),
                ('description', models.CharField(db_index=True, max_length=300, unique=True, verbose_name='Обозначение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_code.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Код',
                'verbose_name_plural': 'Коды',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, related_name='chiled', to='search_code.code', verbose_name='Ребёнок')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='search_code.code', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связи',
                'ordering': ('id',),
            },
        ),
    ]
