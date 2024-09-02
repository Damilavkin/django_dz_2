from django.urls import path
from . import views


app_name = 'task1'

urlpatterns = [
    path('', views.platform, name='platform'),
    path('games/', views.games, name='games'),
    path('cart/', views.cart, name='cart'),
    path('sign_up_django/', views.sign_up_by_django, name='sign_up_django'),
    path('sign_up_html/', views.sign_up_by_html, name='sign_up_html'),

]