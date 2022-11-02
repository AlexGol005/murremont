from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Repair


class MainView(ListView):
    """выводит главную страницу"""
    template_name = 'main/main.html'
    model = Repair
    context_object_name = 'objects'

class OrderView(TemplateView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'





