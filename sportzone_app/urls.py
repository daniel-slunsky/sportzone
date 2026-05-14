from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('rezervovat/', views.vytvorit_rezervaci, name='vytvorit_rezervaci'),
    path('moje-rezervace/', views.moje_rezervace, name='moje_rezervace'),
    path('login/', auth_views.LoginView.as_view(template_name='sportzone_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
