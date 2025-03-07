# serializers.py
from rest_framework import serializers
from Authentication.models import Parker, Landlord

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = '__all__'
