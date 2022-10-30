from django.db import models
from django.core.exceptions import ValidationError

from .mixins import InstancesLimitModelMixin


class ContactsColumnsNumber(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3


class ProjectsColumnsNumber(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3


class HomePageSettingsModel(InstancesLimitModelMixin, models.Model):
    tab_title = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100)
    blue_navbar_button = models.CharField(max_length=100)
    blue_navbar_button_link = models.CharField(max_length=200)
    bigest_title_text = models.TextField(max_length=100)
    bigest_title_text_font_size_in_pixels = models.CharField(max_length=20, default='40px')
    discount_end = models.DateTimeField()
    until_discount_end_text = models.TextField(max_length=500)
    under_bigest_title_text = models.TextField(max_length=500)
    link_to_full_reviews_list = models.URLField()
    contacts_columns_number = models.IntegerField(default=1, choices=ContactsColumnsNumber.choices)
    projects_columns_number = models.IntegerField(default=1, choices=ProjectsColumnsNumber.choices)
    slogan = models.TextField(max_length=100)


class ProjectModel(models.Model):
    description = models.CharField(max_length=100)
    preview_image = models.ImageField()


class ContactModel(InstancesLimitModelMixin, models.Model):
    instances_limit = 3
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=50)


class ReviewModel(InstancesLimitModelMixin, models.Model):
    instances_limit = 3
    reviewer_name = models.CharField(max_length=200)
    reviews_text = models.TextField(max_length=1000)


class WhyUsModel(InstancesLimitModelMixin, models.Model):
    first_argument = models.TextField(max_length=200)
    second_argument = models.TextField(max_length=200)
    third_argument = models.TextField(max_length=200)


class SeoModel(InstancesLimitModelMixin, models.Model):
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    keywords = models.CharField(max_length=1000)