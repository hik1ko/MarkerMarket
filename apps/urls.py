from django.urls import path

from apps.views import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]
