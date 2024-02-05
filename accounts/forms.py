from django.contrib.auth.forms import UserCreationForm,UserChangeForm # foydalanuvchini royxatdan otkazish froma 
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):# meta class qoshimcha asosiysiga 
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)# foydalanuchining ma'lumotlari
class CustomUserChangeForm(UserChangeForm):# foydalanuvchining ma'lumotlarini ozgartirsih
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','age',)