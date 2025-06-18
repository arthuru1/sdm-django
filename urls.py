from django.urls import path
from . import views

urlpatterns = [
    path('', views.sdm_list, name='sdm_list'),
    path('tambah/', views.sdm_create, name='sdm_create'),
    path('edit/<int:pk>/', views.sdm_update, name='sdm_update'),
    path('hapus/<int:pk>/', views.sdm_delete, name='sdm_delete'),
]
