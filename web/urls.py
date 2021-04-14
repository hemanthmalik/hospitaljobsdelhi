from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name="web/about_us.html"), name='about'),
    path('services/', TemplateView.as_view(template_name='web/services.html'), name='services'),
    path('blog/', TemplateView.as_view(template_name='web/blog.html'), name='blog'),
    path('gallery/', TemplateView.as_view(template_name='web/gallery.html'), name='gallery'),
    path('contact/', TemplateView.as_view(template_name='web/contact_us.html'), name='contact'),
    path('register/', views.register, name='register'),
    path('recruit/', views.recruit, name="recruit"),
    path('<int:jid>/get_resume/', views.get_resume, name="get_resume")
]