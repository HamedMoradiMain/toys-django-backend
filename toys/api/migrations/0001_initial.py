# Generated by Django 5.0.1 on 2024-01-28 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'toyCategories',
            },
        ),
        migrations.CreateModel(
            name='Toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('relase_date', models.DateTimeField()),
                ('was_included_in_home', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('toy_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.toycategory')),
            ],
        ),
    ]
