
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('ajuda/', TemplateView.as_view(template_name='ajuda.html'), name='ajuda'),
    path('fale-conosco/', views.ViewFaleConosco.as_view(), name='fale_conosco'),
]
