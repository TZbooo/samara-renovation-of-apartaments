from django.db import migrations

from home.models import SeoModel


def create_default_seo_model(*args, **kwargs):
    SeoModel.objects.create(
        author='Владелец компании по ремонту в Самаре',
        description='Ремонт квартир и все виды отделки в Самаре',
        keywords='Ремонт,Квартиры,Самара,Отделка',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0022_seomodel'),
    ]

    operations = [
        migrations.RunPython(create_default_seo_model),
    ]