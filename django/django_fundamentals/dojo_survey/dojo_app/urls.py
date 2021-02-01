from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processing', views.processing),
    path('results/<name>/<location>/<language>/<comments>', views.results)
]