from django.urls import path, include
from images import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_images),
    path('all/', views.get_all_images),
]
