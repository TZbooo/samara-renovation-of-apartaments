from django.db import migrations

from home.models import WhyUsModel


def create_why_use_arguments(*args, **kwargs):
    WhyUsModel.objects.create(
        first_argument='Предоплата только 20%',
        second_argument='Проверенные поставщики\nматериалов',
        third_argument='Работаем по закону и с договором',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0019_whyusmodel'),
    ]

    operations = [
        migrations.RunPython(create_why_use_arguments),
    ]