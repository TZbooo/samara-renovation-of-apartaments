from django.views.generic import TemplateView

from .models import HomePageSettingsModel
from .models import ProjectModel
from .models import ReviewModel
from .models import ContactModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = HomePageSettingsModel.objects.get()
        context['projects'] = ProjectModel.objects.all()
        context['contacts'] = ContactModel.objects.all()
        context['reviews'] = ReviewModel.objects.all()
        return context
    