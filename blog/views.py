from django.shortcuts import render
from django.views.generic import TemplateView

class BaseTemplate(TemplateView):
  template_name='base.html'

class HomeView(TemplateView):
  template_name='blog/home.html'

class AboutView(TemplateView):
  template_name='blog/about.html'


# Create your views here.
