from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, Second_name,Third_name,Fourth_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not Second_name:
            raise ValueError("User must have a second name")
        if not Third_name:
            raise ValueError("User must have a Third name")
        if not Fourth_name:
            raise ValueError("User must have a Fourth name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.Second_name = Second_name
        user.Third_name = Third_name
        user.Fourth_name = Fourth_name
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, Second_name,Third_name,Fourth_name,phone_number, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not Second_name:
            raise ValueError("User must have a second name")
        if not Third_name:
            raise ValueError("User must have a Third name")
        if not Fourth_name:
            raise ValueError("User must have a Fourth name")
        if not phone_number:
            raise ValueError("User must have a phone number")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.Second_name = Second_name
        user.Third_name = Third_name
        user.Fourth_name = Fourth_name
        user.phone_number=phone_number
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, Second_name,Third_name,Fourth_name,phone_number,  password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not Second_name:
            raise ValueError("User must have a second name")
        if not Third_name:
            raise ValueError("User must have a Third name")
        if not Fourth_name:
            raise ValueError("User must have a Fourth name")
        if not phone_number:
            raise ValueError("User must have a phone number")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.Second_name = Second_name
        user.Third_name = Third_name
        user.Fourth_name = Fourth_name
        user.phone_number=phone_number
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    USER_TYPE_ADMIN=0
    USER_TYPE_ORGANIZATION=1
    USER_TYPE_EVALUATOR=3
    USER_TYPE_CUSTOMER=4
    USER_TYPE_CHOICES = (
        (USER_TYPE_ADMIN, 'Admin'),
        (USER_TYPE_ORGANIZATION, 'ORGANIZATION'),
        (USER_TYPE_EVALUATOR, 'EVALUATOR'),
        (USER_TYPE_CUSTOMER, 'CUSTOMER'),

    )
    address         = models.CharField(max_length=90,null=True)
    GENDER_CHOICES  = ((0, 'Female'),(1, 'Male'), )
    date_of_birth   = models.DateField(blank=True, null=True)
    gender          = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    user_type       = models.IntegerField(default=USER_TYPE_ADMIN, choices=USER_TYPE_CHOICES)
    email           = models.EmailField('email address', unique=True)
    first_name      = models.CharField('first name', max_length=30)
    Second_name     = models.CharField('second name', max_length=30)
    Third_name      = models.CharField('Third name', max_length=30)
    Fourth_name     = models.CharField('Fourth name', max_length=30)
    phone_number    = models.CharField('Phone Number', max_length=15)
    Business_name   = models.CharField(max_length=90,null=True,blank=True,)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    # groups = models.OneToOneField(Group)
    # user_permissions =User.user_permissions
    # groups=User.groups

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'Second_name','Third_name','Fourth_name','phone_number',]

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    # @staticmethod
    # def has_module_perms(app_label):
    #     # "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    def __str__(self):
        return "{}".format(self.email)
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    
