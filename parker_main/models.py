from django.db import models

# Create your models here.
from django.shortcuts import render
from Authentication.models import Landlord

def Parker_main(request):
    landlords = Landlord.objects.all()  # Fetch all landlords
    return render(request, 'parker_main.html', {'landlords': landlords})
