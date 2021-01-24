from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('recruit/', views.recruit, name="recruit")
]