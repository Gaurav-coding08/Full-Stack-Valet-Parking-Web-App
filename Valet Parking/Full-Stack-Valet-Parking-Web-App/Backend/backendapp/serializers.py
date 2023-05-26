from rest_framework import serializers
from backendapp.models import Car_info,Admin_info

class Car_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car_info
        fields="__all__"
        
class Admin_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin_info
        fields="__all__"