from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.forms import RegisterForm


# Create your views here.


class HomeView(TemplateView):
    template_name = 'apps/main/index.html'


class RegisterFormView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'apps/auth/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')
