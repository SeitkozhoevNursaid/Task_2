from django.urls import path
from . import views

urlpatterns = [
    path('api/product/',views.get_products),
    path('api/product/detail/<int:pk>/',views.get_detail),
    path('api/product/create/',views.add_products),
    path('api/product/<int:pk>/update/',views.update_products),
    path('api/product/<int:pk>/delete/',views.delete_products),
    
    path('api/category/',views.get_category),
    path('api/category/detail/<int:pk>/',views.get_detail_category),
    path('api/category/create/',views.add_category),
    path('api/category/<int:pk>/update/',views.update_category),
    path('api/category/<int:pk>/delete/',views.delete_category),
    
    
    
    ]
