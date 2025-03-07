from django.db import models

class Parker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=[('car', 'Car'), ('bike', 'Bike')], default="car")
    vehicle_number = models.CharField(max_length=20, unique=True)  # Correct field name
    pin = models.CharField(max_length=4)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"
    
# models.py



from django.db import models

class Landlord(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    area = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin = models.CharField(max_length=255)  # Password
    latitude = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    profile_image = models.ImageField(upload_to='landlord_images/', null=True, blank=True)

    def __str__(self):
        return self.name
