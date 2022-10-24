from django.db import migrations
from django.utils import timezone as tz
from home.models import HomePageSettingsModel


def create_default_settings(*args, **kwargs):
    HomePageSettingsModel.objects.create(
        tab_title='Ремонт квартир',
        phone_number='8 (920) 452 01-88',
        blue_navbar_button='позвони мне',
        blue_navbar_button_link='https://youtube.com',
        bigest_title_text='Ремонт квартир',
        discount_end=tz.now(),
        until_discount_end_text='до конца скидки 10% осталось',
        under_bigest_title_text='поделись с другом и получи скидку 10%',
        link_to_full_reviews_list='https://youtube.com',
        brand_name='REMONT.RU',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0015_homepagesettingsmodel_brand_name_and_more'),
    ]
    operations = [
        migrations.RunPython(create_default_settings),
    ]