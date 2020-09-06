from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<image_id>/', views.one_image)
]