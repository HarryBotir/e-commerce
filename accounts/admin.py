from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserCreationForm
    list_display = ['email','username','first_name','last_name','age','is_staff'] #barcha ma'lumotlarni ko'rsatish uchun qo'shildi 
    fieldsets = UserAdmin.fieldsets +(
        (None,{'fields':('age',)}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None,{'fields':('age',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)