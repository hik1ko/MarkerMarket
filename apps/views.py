from django.views.generic import TemplateView

from apps.models import Product


class HomeView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/index.html'
