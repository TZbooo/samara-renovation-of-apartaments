from django.views.generic import TemplateView


class RobotsTXTView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
