from django.urls import path
from parker_main import views

urlpatterns = [

    path('', views.Parker_main, name='Parker_main'),

]
