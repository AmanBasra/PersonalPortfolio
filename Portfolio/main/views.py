from django.shortcuts import render
from django.views.generic import TemplateView


class home(TemplateView):
    template_name='home.html'


class aboutme(TemplateView):
    template_name='aboutme.html'

class portfolio(TemplateView):
    template_name='portfolio.html'

class contactme(TemplateView):
    template_name='contactme.html'