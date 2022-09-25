from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('1', views.TestView.as_view(), name='test'),
      ]
