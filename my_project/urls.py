"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello_world import views as index_views
from about import views as about_me


urlpatterns = [
    # O Django verifica se é '' (a raiz ou meusite.com/). Se for, ele executa index_views.index e para
    path(' ', index_views.index, name='index'),
    path('about/', about_me.index, name='about'),
    # Se não for, ele verifica se a URL começa com admin/. Se for, ele envia o controle para o módulo de administração e para.
    path('admin/', admin.site.urls),
]
# Se nenhuma correspondência for encontrada, o Django retorna um erro 404 (Página não encontrada).
