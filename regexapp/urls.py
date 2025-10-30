from django.urls import path
from . import views

urlpatterns = [
    path('', views.regex_tool, name='regex_tool'),
]