from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Make sure this matches your view
]
