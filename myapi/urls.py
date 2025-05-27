"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path, include
from myapi.views import ProductView, users, login, CategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductView, basename='product')

urlpatterns = [
    path('users/', users),
    path('users/<int:id>/', users),
    path('login/', login),
    path('categories/', CategoryView.as_view()),
    path('categories/<int:id>/', CategoryView.as_view()),
    path('myproducts/', include(router.urls))
    ]
