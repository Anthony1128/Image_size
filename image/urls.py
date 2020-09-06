from django.urls import path
from . import views


app_name = 'image'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_image/', views.new_image, name='new_image'),
    path('<image_id>/', views.one_image, name='one_image'),
]