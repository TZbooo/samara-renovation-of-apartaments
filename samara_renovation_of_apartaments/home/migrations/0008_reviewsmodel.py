# Generated by Django 4.1.2 on 2022-10-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepagesettingsmodel_discount_end'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=200)),
                ('reviews_text', models.TextField(max_length=1000)),
            ],
        ),
    ]
