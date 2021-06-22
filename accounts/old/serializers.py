from rest_framework import serializers
from .models import CustomUser
class customUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'Second_name', 'Third_name', 'Fourth_name',
                  'phone_number','password']

class organizationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'Second_name', 'Third_name', 'Fourth_name',
                  'phone_number','address','Business_name','password']