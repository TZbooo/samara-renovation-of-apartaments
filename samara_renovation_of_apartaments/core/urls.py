from django.urls import path

from core.views import RobotsTXTView


urlpatterns = [
    path('robots.txt/', RobotsTXTView.as_view(), name='robots.txt'),
]
