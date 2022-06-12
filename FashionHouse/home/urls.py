from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
]