
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajuda/', TemplateView.as_view(template_name='ajuda.html'), name='ajuda'),
    path('fale-conosco/', views.ViewFaleConosco.as_view(), name='fale_conosco'),
    path('carrinho/', include('carrinho.urls', namespace='carrinho')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
    path('', include('main.urls', namespace='main')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
