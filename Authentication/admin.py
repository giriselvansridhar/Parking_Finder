


from django.contrib import admin
from .models import Landlord,Parker  # Import the Landlord model

# Register the Landlord model to the admin site
admin.site.register(Landlord)
admin.site.register(Parker)