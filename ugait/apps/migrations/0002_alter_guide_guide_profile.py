# Generated by Django 4.0.2 on 2022-07-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='guide_profile',
            field=models.ImageField(blank=True, null=True, upload_to='guide_photo'),
        ),
    ]