from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Repair


class MainView(TemplateView):
    """выводит главную страницу"""
    template_name = 'main/main.html'

class OrderView(ListView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'
    model = Repair
    context_object_name = 'objects'




