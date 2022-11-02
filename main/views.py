from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Repair


class MainView(ListView):
    """выводит главную страницу"""
    model = Repair
    template_name = 'main/main.html'
    context_object_name = 'objects'
    paginate_by = 20

class OrderView(TemplateView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'





