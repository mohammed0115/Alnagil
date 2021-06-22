from phone.serializers import PhoneNumberSerializer
from phone.models import PhoneNumber
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
import pyotp
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import HasValidAPIKey
from .models import *
from accounts.models import CustomUser
from django.contrib.auth import authenticate, login
from .auth.utils import get_access_token
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,UserSerializer_,forgetPasswordSerializer,ChangePasswordSerializer
from rest_framework import viewsets
from APIKEY.models import APIKey

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
import base64
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.pagination import  PageNumberPagination

from phone.models import PhoneNumber,Country
from phone.views import generateKey



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class completProfile(APIView):
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    authentication_classes = ()
    # permission_classes = (HasValidAPIKey,IsAuthenticated)
    permission_classes = ()
    """{
            "email":"",
            "first_name":"",
            "Second_name":"",
            "Third_name":"",
            "Fourth_name":"",
            "phone_number":"",
            "address":"",
            "password":"",
            "user_type":"",
            "Business_name":""
        }"""
    def post(self, request, format=None):
        
        try:
            data= request.data
            required =['email', 'first_name', 'Second_name', 'Third_name', 'Fourth_name',
                  'phone_number','address','Business_name','password','user_type']
            isRequiredList=[]
            for i in  required:
                if i not in data:
                    isRequiredList.append({"["+i+"]":""" "field  is required." """})
            if len(isRequiredList)!=0:
                return Response({"Error":isRequiredList})
            else:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user=CustomUser.objects.get(**serializer.data)
                    token=Token.objects.create(user=user)
                    return Response({"status":"success","data":serializer.data,"token":token.key}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"status":"failed","error":serializer.errors})
        except Exception as identifier:
            return Response({"status":"failed","message":str(identifier)})
            
        


class login(APIView):
    authentication_classes = ()
    permission_classes = (HasValidAPIKey,)
    def post(self,request):
        try:
            data= request.data
            required =['email','phone','password','user_type']
            isRequiredList=[]
            for i in  required:
                if i not in data:
                    isRequiredList.append({"["+i+"]":"field  is required."})
            if len(isRequiredList)!=0:
                return Response({"Error":isRequiredList})
            else:
                if data['email']=="" and data['phone']=="":
                    return Response({"status":"failed","message":"email field or phone should not be empty"})
                else:
                    serializer=UserSerializer_(data=data)
                    if serializer.is_valid():
                        user=authenticate(**serializer.data)
                        token=Token.objects.get(user=user)
                        return Response({"status":"success","data":serializer.data,"token":token.key})
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as identifier:
            return Response({"status":"failed","message":str(identifier)})
class resetPassword(APIView):
    authentication_classes = ()
    permission_classes = ()
    def get_object(self, data):
        try:             
            return CustomUser.objects.get(**data)
        except CustomUser.DoesNotExist as identifier:
            return Response({"status":"failed","message1":str(identifier)})
    def post(self,request):
        # try:
            data= request.data
            print('password' not in data)
            required =['email','phone','password','user_type']
            isRequiredList=[]
            for i in  required:
                print(i not in data)
                if i not in data:
                    isRequiredList.append({"["+i+"]":""" "field  is required..." """})
            if len(isRequiredList)!=0:
                return Response({"Error":isRequiredList})
            else:
                if data['email']=="" and data['phone']=="":
                    return Response({"status":"failed","message":"email field or phone should not be empty"})
                else:
                    indent={'user_type':data['user_type']}
                    if data['phone']=="":
                        indent['email']=data['email']
                    else:
                        indent['phone']=data['phone']
                    user=self.get_object(indent)
                    print("data is ready",data)
                    serializer=ChangePasswordSerializer(user,data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status":"success","data":serializer.data})
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as identifier:
        #     return Response({"status":"failed","message":str(identifier)})
        

class ForgetPassword(APIView):
    permission_classes = (HasValidAPIKey,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            data= request.data
            required =['email','phone','user_type']
            isRequiredList=[]
            for i in  required:
                if i not in data:
                    isRequiredList.append({"["+i+"]":""" "field  is required." """})
            if len(isRequiredList)!=0:
                return Response({"Error":isRequiredList})
            else:
                if data['email']=="" and data['phone']=="":
                    return Response({"status":"failed","message":"email field or phone should not be empty"})
                else:
                    phone=data['phone']
                    if phone:
                        pass
                    else:
                        user=CustomUser.objects.get(email=data['email'],user_type=data['user_type'])
                        phone=user.phone
                    try:
                        Mobile = PhoneNumber.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
                    except ObjectDoesNotExist:
                        PhoneNumber.objects.create(
                            Mobile=phone,
                        )
                        Mobile = PhoneNumber.objects.get(Mobile=phone)  # user Newly created Model
                    Mobile.counter += 1  # Update Counter At every Call
                    Mobile.save()  # Save the data
                    keygen = generateKey()
                    key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
                    OTP = pyotp.HOTP(key,4)  # HOTP Model for OTP is created
                    print(OTP.at(Mobile.counter))
                    # here send email
                    # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
                    return Response({"status":"success","otp": OTP.at(Mobile.counter)}, status=200)
        except Exception as identifier:
            return Response({"status":"failed","message":str(identifier)})        
        

class LogoutUserView(APIView):
    permission_classes = (HasValidAPIKey, IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        current_token = get_access_token(request)
        BlockedToken.objects.create(token=current_token)
        return Response()