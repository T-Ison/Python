from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<id>', views.showDetail),
    path('shows/<id>/edit', views.editShow),
    path('shows/<id>/update', views.updateShow),
    path('shows/<id>/destroy', views.destroyShow),
    # path('shows/<id>/addNetwork', views.addNetwork),
]
