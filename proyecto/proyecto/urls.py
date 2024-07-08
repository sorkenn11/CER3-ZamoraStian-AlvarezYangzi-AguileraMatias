"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from myapp import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('',views.inicio,name='inicio'),
    path('access_denied/', views.access_denied_view, name='access_denied'),  # Añade esta línea
    path('producciones/', views.lista_producciones_view, name='lista_producciones'),
    path('producciones/editar/<int:pk>/', views.editar_produccion_view, name='editar_produccion'),
    path('panel/', views.panel_operador_view, name='panel'),
    path('api-auth/', include('rest_framework.urls')), #para navegar la API(mati)
    path('api/',include('myapp.urls')),
    ]
