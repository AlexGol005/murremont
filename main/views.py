from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView

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



class OrderView(SuccessMessageMixin, CreateView):
    """выводит страницу заказа"""
    template_name = 'main/order.html'
    success_message = "Заявка успешно отправлена! Оператор свяжется с вами"
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['title'] = Repair.objects.get(pk=self.kwargs['pk']).name
        return context

    def form_valid(self, form):
        order = form.save(commit=False)
        order.repair = Repair.objects.get(pk=self.kwargs['pk']).name
        order.save()
        return redirect('/sucsess')

class SucsessView(TemplateView):
    """ Представление, которое выводит подтверждение отправки заявки покупателю"""
    template_name = 'main/sucsess.html'






