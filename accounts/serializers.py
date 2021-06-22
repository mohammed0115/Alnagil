from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
from accounts.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','email', 'first_name', 'Second_name', 'Third_name', 'Fourth_name',
                  'phone_number','address','Business_name','password','user_type')
class UserSerializer_(serializers.Serializer):
    email = serializers.EmailField( allow_blank=True,allow_null=True)
    phone = serializers.CharField(max_length=13,allow_blank=True,allow_null=True)
    password = serializers.CharField(max_length=200)
    user_type     = serializers.IntegerField

class forgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField( allow_blank=True,allow_null=True)
    phone = serializers.CharField(max_length=13,allow_blank=True,allow_null=True)
    # password = serializers.CharField(max_length=200)
    user_type     = serializers.IntegerField()


class ChangePasswordSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)
    # email = serializers.EmailField( allow_blank=True,allow_null=True)
    # phone = serializers.CharField(max_length=13,allow_blank=True,allow_null=True)
    # password = serializers.CharField(max_length=200)
    # user_type     = serializers.IntegerField()
    
    # old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'password','user_type')
        # read_only_fields = ['Business_name',]

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    # def validate_old_password(self, value):
    #     user = self.context['request'].user
    #     if not user.check_password(value):
    #         raise serializers.ValidationError({"old_password": "Old password is not correct"})
    #     return value

    def update(self, instance, validated_data):
        print(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()

        return instance