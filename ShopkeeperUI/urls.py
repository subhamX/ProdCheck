from django.urls import path
from ShopkeeperUI import views

urlpatterns = [
    path('', views.home),
    path('shophome/', views.shopHome),
    path('userhome/', views.userHome),
    path('shophome/additem/', views.addItem, name='additem'),
    path('shophome/addshop/', views.addShop, name='addshop'),
    path('shophome/<int:value>/', views.shopDetail, name='shoplink')
]