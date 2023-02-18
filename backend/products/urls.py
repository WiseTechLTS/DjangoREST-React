from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.user_products),
    path('all/', views.get_all_products),
]
