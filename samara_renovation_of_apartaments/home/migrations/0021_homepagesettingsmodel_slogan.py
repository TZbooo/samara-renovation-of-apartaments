# Generated by Django 4.1.2 on 2022-10-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_add_default_why_us_arguments'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettingsmodel',
            name='slogan',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]