from django.shortcuts import render, redirect
from .forms import ParkerSignUpForm
from .forms import LandlordSignUpForm

from .models import Parker, Landlord
from django.contrib import messages

def parker_sign_up(request):
    if request.method == 'POST':
        form = ParkerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign Up Successful! You can now log in.")
            return redirect('Parker_Login')  # Make sure this URL name is correct in urls.py
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ParkerSignUpForm()

    return render(request, 'parker_sign_up.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LandlordSignUpForm


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LandlordSignUpForm


def landlord_signup(request):
    if request.method == "POST":
        form = LandlordSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect after successful signup
    else:
        form = LandlordSignUpForm()

    return render(request, 'landlord_signup.html', {'form': form})

# def landlord_sign_up(request):
#     if request.method == 'POST':
#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             landlord = form.save(commit=False)

#             print("Latitude before saving:", landlord.latitude)  # Debugging
#             print("Longitude before saving:", landlord.longitude)  # Debugging

#             landlord.save()
#             messages.success(request, "Sign Up Successful! You can now log in.")
#             return redirect('LandLord_Login')  
#         else:
#             print(form.errors)  # Debug form errors
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = LandlordSignUpForm()

#     return render(request, 'landlord_signup.html', {'form': form})

# def landlord_sign_up(request):
#     if request.method == 'POST':
#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             landlord = form.save(commit=False)

#             print("Latitude before saving:", landlord.latitude)  # Debugging
#             print("Longitude before saving:", landlord.longitude)  # Debugging

#             landlord.save()
#             messages.success(request, "Sign Up Successful! You can now log in.")
#             return redirect('LandLord_Login')  
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = LandlordSignUpForm()

#     return render(request, 'landlord_signup.html', {'form': form})


# def landlord_sign_up(request):
#     if request.method == 'POST':
#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             landlord = form.save(commit=False)

#             print("Latitude:", landlord.latitude)  # Debugging
#             print("Longitude:", landlord.longitude)  # Debugging

#             landlord.save()
#             messages.success(request, "Sign Up Successful! You can now log in.")
#             return redirect('LandLord_Login')  
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = LandlordSignUpForm()

#     return render(request, 'landlord_signup.html', {'form': form})

# def landlord_sign_up(request):
#     if request.method == 'POST':
#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             landlord = form.save(commit=False)

#             print("Latitude:", landlord.latitude)  # Debugging
#             print("Longitude:", landlord.longitude)  # Debugging

#             landlord.save()
#             messages.success(request, "Sign Up Successful! You can now log in.")
#             return redirect('LandLord_Login')  
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = LandlordSignUpForm()

#     return render(request, 'landlord_signup.html', {'form': form})


# def landlord_sign_up(request):
#     if request.method == 'POST':
#         print("Received POST Data:", request.POST)  # Debugging

#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             landlord = form.save(commit=False)
#             landlord.latitude = request.POST.get('latitude')  # Fetch lat from form
#             landlord.longitude = request.POST.get('longitude')  # Fetch lng from form
#             print("Saving Landlord:", landlord.latitude, landlord.longitude)  # Debugging
#             landlord.save()
#             messages.success(request, "Sign Up Successful! You can now log in.")
#             return redirect('LandLord_Login')
#         else:
#             print("Form Errors:", form.errors)  # Debugging
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = LandlordSignUpForm()
    
#     return render(request, 'landlord_signup.html', {'form': form})


# Create your views here.


# views.py



# views.py


# def landlord_sign_up(request):
#     if request.method == 'POST':
#         form = LandlordSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('LandLord_Login')  # Redirect to login after successful registration
#     else:
#         form = LandlordSignUpForm()
#     return render(request, 'landlord_signup.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Parker

def Login_Parker(request):
    if request.method == "POST":
        # 1. Get Phone Number
        phone = request.POST.get('phone', '').strip()
        print(f"DEBUG: Received Phone Number: '{phone}'")

        # 2. Get PIN Inputs (Handling Missing Fields)
        pin_parts = [request.POST.get(f'pin{i}', '').strip() for i in range(1, 5)]
        pin = "".join(pin_parts)  # Concatenating PIN inputs safely
        print(f"DEBUG: Received PIN Parts: {pin_parts}")
        print(f"DEBUG: Combined PIN: '{pin}'")

        # 3. Check if Inputs are Missing
        if not phone:
            print("DEBUG: Phone number field is empty!")
            messages.error(request, "Phone number is required.")
            return redirect('Parker_main')

        if not all(pin_parts):
            print("DEBUG: One or more PIN fields are empty!")
            messages.error(request, "All PIN fields are required.")
            return redirect('Parker_main')

        try:
            # 4. Check if Parker Exists in Database
            print("DEBUG: Checking if Parker exists...")
            parker = Parker.objects.get(phone=phone)
            print(f"DEBUG: Found Parker with Phone: {parker.phone}, Stored PIN: {parker.pin}")

            # 5. Compare Stored PIN with Entered PIN
            if parker.pin == pin:
                print("DEBUG: PIN Matched! Login Successful.")
                messages.success(request, "Login Successful!")
                return redirect('Parker_main')
            else:
                print("DEBUG: PIN Mismatch! Login Failed.")
                messages.error(request, "Invalid PIN.")
        
        except Parker.DoesNotExist:
            print("DEBUG: No Parker found with this phone number!")
            messages.error(request, "Phone number not registered.")

        print("DEBUG: Redirecting to Parker_Login due to login failure.")
        return redirect('Parker_main')

    print("DEBUG: Rendering Parker Login Page (GET Request).")
    return render(request, 'parker-login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Landlord

def Login_LandLord(request):
    if request.method == 'POST':
        # Debugging Input Values
        phone = request.POST.get('phone', '').strip()
        pin1 = request.POST.get('pin1', '').strip()
        pin2 = request.POST.get('pin2', '').strip()
        pin3 = request.POST.get('pin3', '').strip()
        pin4 = request.POST.get('pin4', '').strip()

        print(f"DEBUG: Received Phone: '{phone}'")
        print(f"DEBUG: PIN Parts -> [{pin1}], [{pin2}], [{pin3}], [{pin4}]")

        # Concatenate PIN
        pin = pin1 + pin2 + pin3 + pin4
        print(f"DEBUG: Combined PIN: '{pin}'")

        # Validate Input
        if not phone or len(pin) != 4:
            print("DEBUG: Missing phone number or PIN fields!")
            messages.error(request, "All fields are required.")
            return redirect('Parker_main')

        # Remove country code if present
        if phone.startswith('+91'):
            phone = phone[3:].strip()
            print(f"DEBUG: Phone after removing +91: '{phone}'")

        try:
            # Check if landlord exists
            print("DEBUG: Searching for landlord in database...")
            landlord = Landlord.objects.get(phone=phone)
            print(f"DEBUG: Found Landlord: {landlord.phone}, Stored PIN: {landlord.pin}")

            # PIN Comparison
            if landlord.pin == pin:
                request.session['landlord_id'] = landlord.id
                print("DEBUG: PIN Matched! Login Successful.")
                messages.success(request, "Login successful!")
                return redirect('Parker_main')
            else:
                print("DEBUG: PIN Mismatch! Login Failed.")
                messages.error(request, "Invalid PIN.")

        except Landlord.DoesNotExist:
            print("DEBUG: No Landlord found with this phone number!")
            messages.error(request, "Phone number not registered.")

        print("DEBUG: Redirecting back to LandLord_Login due to login failure.")
        return redirect('LandLord_Login')

    print("DEBUG: Rendering landlord login page (GET request).")
    return render(request, 'landlord-login.html')


# Define a view for the Parker Sign Up page



def home(request):
    return render(request, 'index.html')





from .models import Parker, Landlord

def dashboard_view(request):
    return render(request, 'dashboard.html', {
        'parkers': Parker.objects.all(),
        'landlords': Landlord.objects.all(),
    })
