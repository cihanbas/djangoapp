from django.urls import path

from . import views

urlpatterns=[
  path('',views.BaseTemplate.as_view(),name='base'),
  path('home/',views.HomeView.as_view(),name='home'),
  path('about/',views.AboutView.as_view(),   name='about'),
  path('contact/',views.ContactView.as_view(),   name='contact'),
]