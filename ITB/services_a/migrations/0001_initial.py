# Generated by Django 5.2.1 on 2025-06-11 19:18

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('service_type', models.CharField(choices=[('corporate', 'Corporate Training'), ('bootcamp', 'Career Bootcamp'), ('certification', 'Certification Prep'), ('internship', 'Internship Program'), ('faculty', 'Faculty Development'), ('lab', 'Lab Infrastructure')], max_length=50)),
                ('icon_class', models.CharField(default='fas fa-circle', max_length=50)),
                ('short_description', models.TextField()),
                ('full_description', ckeditor.fields.RichTextField()),
                ('is_featured', models.BooleanField(default=False)),
                ('badge_text', models.CharField(blank=True, max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('cta_text', models.CharField(default='Learn More', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['display_order', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ServiceFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='services_a.service')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
