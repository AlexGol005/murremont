from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/superbase.html'

class TestView(TemplateView):
    template_name = 'main/test.html'
