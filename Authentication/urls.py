from django.urls import path
from Authentication import views



urlpatterns = [
    path('',views.Login_Parker,name="Parker_Login" ),
    path('Land_Lord_Login/', views.Login_LandLord, name="LandLord_Login"),  
    path('Land_Lord_Register/', views.landlord_signup, name="LandLord_Register"),
    path('Parker_Register/', views.parker_sign_up, name="Parker_Register")
]

