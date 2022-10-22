from django.db import models
from django.core.exceptions import ValidationError


class HomePageSettingsModel(models.Model):
    tab_title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    blue_navbar_button = models.CharField(max_length=100)
    bigest_title_text = models.CharField(max_length=100)
    discount_end = models.DateTimeField()
    until_discount_end_text = models.TextField(max_length=500)
    under_bigest_title_text = models.TextField(max_length=500)

    def clean(self) -> None:
        if not HomePageSettingsModel.objects.filter(pk=self.pk).exists() and \
                HomePageSettingsModel.objects.count():
            raise ValidationError('you must use one settings model')
        return super().clean()


class ProjectModel(models.Model):
    description = models.CharField(max_length=100)
    preview_image = models.ImageField()


class ContactModel(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=50)

    def clean(self) -> None:
        if not ContactModel.objects.filter(pk=self.pk).exists() and \
                ContactModel.objects.count() == 3:
            raise ValidationError('you can\'t create more than 3 model instances')
        return super().clean()


class ReviewModel(models.Model):
    reviewer_name = models.CharField(max_length=200)
    reviews_text = models.TextField(max_length=1000)

    def clean(self) -> None:
        if not ReviewModel.objects.filter(pk=self.pk).exists() and \
                ReviewModel.objects.count() == 3:
            raise ValidationError('you can\'t create more than 3 model instances')
        return super().clean()