# Generated by Django 4.1.2 on 2022-10-22 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_contacts_contactmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectsModel',
            new_name='ProjectModel',
        ),
        migrations.RenameModel(
            old_name='ReviewsModel',
            new_name='ReviewModel',
        ),
    ]
