from django.contrib import admin

# Register your models here.from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAdmin(UserAdmin):
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password','phone_number','first_name', 'Second_name','Third_name','Fourth_name',
                    'address','date_of_birth','gender','user_type','Business_name')}),
       ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups','user_permissions'
                                      )}),
      
    )
    filter_horizontal=('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','phone_number','first_name',
                    'Second_name','Third_name','Fourth_name',
                    'address','date_of_birth','gender','user_type','Business_name')
    list_filter = ('email', 'is_staff', 'is_active','user_type')
    def get_fieldsets(self, request, obj=None):
        if obj:
            return self.fieldsets
        else:
            return self.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)