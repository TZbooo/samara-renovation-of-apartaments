from django.contrib import admin

from .models import HomePageSettingsModel
from .models import ProjectModel
from .models import ReviewModel
from .models import ContactModel
from .models import WhyUsModel
from .models import SeoModel


admin.site.register(HomePageSettingsModel)
admin.site.register(ProjectModel)
admin.site.register(ReviewModel)
admin.site.register(ContactModel)
admin.site.register(WhyUsModel)
admin.site.register(SeoModel)