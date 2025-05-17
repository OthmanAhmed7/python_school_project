from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_product, name='upload_product'),  # For custom upload form
]