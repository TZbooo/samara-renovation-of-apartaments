# Generated by Django 4.1.2 on 2022-10-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_homepagesettingsmodel_brand_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettingsmodel',
            name='projects_columns_number',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three')], default=1),
        ),
    ]
