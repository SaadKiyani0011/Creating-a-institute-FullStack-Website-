# Generated by Django 5.2.1 on 2025-06-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
