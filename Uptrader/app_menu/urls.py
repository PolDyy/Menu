from django.urls import path

from .views import MainPageView


urlpatterns = [
    path('menu/', MainPageView.as_view(), name='main')
]
