from django.views.generic import TemplateView, ListView

from main.forms import SearchForm, OrderForm
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

class SearchResultView(TemplateView):
    """ Представление, которое выводит результаты поиска на главной странице"""
    template_name = 'main/listmain.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultView, self).get_context_data(**kwargs)
        sword = self.request.GET['sword']
        objects = Repair.objects.filter(name__icontains=sword)
        context['form'] = SearchForm
        context['objects'] = objects
        return context



class OrderView(TemplateView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['form'] = OrderForm
        return context
