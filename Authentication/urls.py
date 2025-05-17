from django.urls import path
from Authentication import views



urlpatterns = [
    path('',views.Login_Parker,name="Parker_Login" ),
    path('Land_Lord_Register/', views.landlord_signup, name="LandLord_Register"),
    path('Parker_Register/', views.parker_sign_up, name="Parker_Register"),
    path("home/", views.home, name="home"),
    path('dashboard/', views.dashboard_view, name='dashboard')
]

