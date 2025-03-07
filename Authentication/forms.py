from django import forms
from .models import Parker
from .models import Landlord
class ParkerSignUpForm(forms.ModelForm):
    class Meta:
        model = Parker
        # Corrected field names
        fields = ['name', 'email', 'phone', 'vehicle_type', 'vehicle_number', 'pin']
        widgets = {
            'pin': forms.PasswordInput(),  # Use PasswordInput for pin if you want to hide it
        }

    def clean_pin(self):
        pin = self.cleaned_data.get('pin')
        if len(pin) != 4 or not pin.isdigit():
            raise forms.ValidationError("PIN must be a 4-digit number.")
        return pin

# forms.py



from django import forms
from .models import Landlord

from django import forms
from .models import Landlord

class LandlordSignUpForm(forms.ModelForm):
    confirm_pin = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Confirm your password'}),
    )

    latitude = forms.DecimalField(
        max_digits=12, decimal_places=10,
        widget=forms.HiddenInput(), required=False
    )
    longitude = forms.DecimalField(
        max_digits=13, decimal_places=10,
        widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = Landlord
        fields = [
            'name', 'email', 'phone', 'pincode', 'address', 'area', 'landmark', 
            'city', 'state', 'country', 'pin', 'confirm_pin', 'latitude', 'longitude', 'profile_image'
        ]
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'pincode': 'Pincode',
            'address': 'Street Address',
            'area': 'Area',
            'landmark': 'Landmark',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'pin': 'Password',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your phone number'}),
            'pincode': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your area pincode'}),
            'address': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your address'}),
            'area': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your area'}),
            'landmark': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter a nearby landmark'}),
            'city': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your city'}),
            'state': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your state'}),
            'country': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your country'}),
            'pin': forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter a secure password'}),
            'latitude': forms.NumberInput(attrs={'step': '0.0000000001'}),
            'longitude': forms.NumberInput(attrs={'step': '0.0000000001'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.replace("+", "").isdigit() or len(phone) not in [10, 12]:
            raise forms.ValidationError("Enter a valid phone number with 10 or 12 digits.")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("pin")
        confirm_pin = cleaned_data.get("confirm_pin")

        if pin and confirm_pin and pin != confirm_pin:
            self.add_error('confirm_pin', "Passwords do not match.")

        return cleaned_data
