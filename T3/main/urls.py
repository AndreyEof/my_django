from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='home'),
    path('/about', views.about, name='about'),
    path('/create_ticket', views.create_ticket, name='crt_tik')
    ]
