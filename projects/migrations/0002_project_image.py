# Generated by Django 4.2.7 on 2024-01-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='Proj_images/'),
        ),
    ]
