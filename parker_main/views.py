from django.shortcuts import render
from Authentication.models import Landlord
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def Parker_main(request):
    try:
        user_lat = float(request.GET.get('lat'))
        user_lon = float(request.GET.get('lon'))
    except (TypeError, ValueError):
        user_lat = 13.0827  # Default to Chennai
        user_lon = 80.2707

    all_landlords = Landlord.objects.exclude(latitude__isnull=True, longitude__isnull=True)

    landlords_with_distance = sorted(
        all_landlords,
        key=lambda l: haversine(user_lat, user_lon, float(l.latitude), float(l.longitude))
    )

    nearest_landlords = landlords_with_distance[:10]

    return render(request, 'parker_main.html', {
        'landlords': nearest_landlords,
        'user_lat': user_lat,
        'user_lon': user_lon
    })
