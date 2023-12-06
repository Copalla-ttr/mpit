from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('what_is', views.what_is),
    path('wallet', views.wallet),
    path('categories', views.categories),
    path('tasks', views.tasks),
    path('partners', views.partners),
]
