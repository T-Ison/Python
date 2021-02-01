from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processing', views.processing),
    path('prt2/<name>/<int:age>/<email>/<password>', views.prt2),
]