from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from apps.forms import RegisterForm
from apps.models import Product


# Create your views here.


class HomeView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/main/index.html'
    context_object_name = 'products'


class RegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'apps/auth/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')
