from django.urls import path,include
from . import views
from .views import*

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('success/', views.success, name="success"),
    path('services/', views.services, name="services"),
    path('aboutus/', views.aboutus, name="aboutus"),
    
    path('data/', views.data, name="data"),
    path('data/<int:id>', views.data_view, name="data_view"),
    path('test/', views.test, name="test"),
]
