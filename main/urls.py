from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('order/<int:pk>', views.OrderView.as_view(), name='order'),
    path('result/', views.SearchResultView.as_view(), name='serres'),
    path('result/', views.SearchResultView.as_view(), name='serres'),
    path('sucsess/', views.SucsessView.as_view(), name='sucsess'),
      ]
