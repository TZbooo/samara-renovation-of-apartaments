# Generated by Django 4.1.2 on 2022-10-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_reviewsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettingsmodel',
            name='under_bigest_title_text',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepagesettingsmodel',
            name='until_discount_end_text',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]