from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset_session', views.reset_session),
]