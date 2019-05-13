from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.Login),
    path('signup/', views.signup),
    path('logout/', views.Logout, name='Logout'),
]