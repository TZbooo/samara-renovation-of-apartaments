# Generated by Django 4.1.2 on 2022-10-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_homepagesettingsmodel_under_bigest_title_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagesettingsmodel',
            name='under_bigest_title_text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='homepagesettingsmodel',
            name='until_discount_end_text',
            field=models.TextField(max_length=500),
        ),
    ]
