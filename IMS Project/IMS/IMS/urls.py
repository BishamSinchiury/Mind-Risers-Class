"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin #type: ignore
from django.urls import path, include #type: ignore
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product-type/', views.ProductTypeApiView.as_view({'get':'list', 'post':'create'})),
    path('product-type/<int:pk>/',views.ProductTypeApiView.as_view({'get':'retrive','put':'update','delete':'destroy'})),
    path('product/', views.ProductApiView.as_view()),
    path('product/<int:pk>/', views.ProductDetailApiView.as_view())


]
