from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.forms import SearchForm
from main.models import Repair


class MainView(ListView):
    """выводит главную страницу"""
    model = Repair
    template_name = 'main/main.html'
    context_object_name = 'objects'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

class OrderView(TemplateView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'





