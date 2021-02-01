from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wall', views.wall),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('postMessage', views.postMessage),
    path('postComment/<int:id>', views.postComment),
    path('deleteMessage/<int:id>', views.deleteMessage),
    path('logout', views.logout),
]
