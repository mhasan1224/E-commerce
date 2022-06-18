from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='products'),
    path('product_details/', views.product_details, name='product_details'),
    path('shop', views.shop, name='shop')
]