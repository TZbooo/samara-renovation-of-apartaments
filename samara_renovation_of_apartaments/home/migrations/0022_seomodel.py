# Generated by Django 4.1.2 on 2022-10-30 12:59

from django.db import migrations, models
import home.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_homepagesettingsmodel_slogan'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('keywords', models.CharField(max_length=1000)),
            ],
            bases=(home.mixins.InstancesLimitModelMixin, models.Model),
        ),
    ]
