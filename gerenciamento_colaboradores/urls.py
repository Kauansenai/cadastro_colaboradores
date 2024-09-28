from django.contrib import admin
from django.urls import path, include
from colaboradores import views

urlpatterns = [
    path('', views.home, name='home'),  # Adiciona a página inicial
    path('admin/', admin.site.urls),
    path('colaboradores/', include('colaboradores.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('emprestimos/', include('emprestimos.urls')),
]
