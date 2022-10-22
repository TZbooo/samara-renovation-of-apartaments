from django.contrib import sitemaps
from django.urls import reverse_lazy


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse_lazy(item)