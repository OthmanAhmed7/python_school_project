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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from school.views import home
from school.views import contact_us
from school.views import welcome
from products.views import home as prod_home
from products.views import contact_us as prod_con
from products.views import welcome as prod_wel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('school/home/', home, name='home'),
    path('school/contact/', contact_us, name='contact'),
    path('school/welcome/', welcome, name='welcome'),
    path('products/home/', prod_home, name='home'),
    path('products/contact/', prod_con, name='contact'),
    path('products/welcome/', prod_wel, name='welcome'),
    path('products/', include('products.urls')),
    path('myapi/', include('myapi.urls')),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
