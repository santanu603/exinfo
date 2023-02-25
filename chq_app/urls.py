from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('entry/', views.entry, name='entry'),
    path('view_update/', views.view_update, name='view_update'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('filter/', views.filter_chq, name='filter_chq'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delivery_management/',views.delivery_main, name='delivery_main'),
    path('filter_delivery/',views.filter_delivery,name='filter_delivery'),
    path('edit_delivery/<int:id>/', views.edit_delivery, name='edit_delivery'),
    path('replacement_main/',views.replacement_main,name='replacement_main'),
    path('filter_replacement/',views.filter_replacement, name='filter_replacement'),
    path('edit_replacement/<int:id>',views.edit_replacement, name='edit_replacement'),
    path('delete_delivery/<int:id>/',views.delete_delivery, name='delete_delivery'),
    path('delete_replacement/<int:id>',views.delete_replacement, name='delete_replacement')
]