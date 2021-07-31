from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Bacsi,Donviyte
from django.forms import ModelForm

class BacsiSignUpForm(UserCreationForm):
    ten=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    motacongviec=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user=super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.phone=self.cleaned_data.get('phone')
        user.motacongviec=self.cleaned_data.get('motacongviec')
        user.is_bacsi= True
        user.save()
        bacsi=Bacsi.objects.create(user=user)
        bacsi.ten=self.cleaned_data.get('ten')
        bacsi.save()
        return bacsi

class DonviyteSignupForm(UserCreationForm):
    ten = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    motacongviec = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.motacongviec = self.cleaned_data.get('motacongviec')
        user.is_donviyte = True
        user.save()
        donviyte = Donviyte.objects.create(user=user)
        donviyte.ten = self.cleaned_data.get('ten')
        donviyte.save()
        return donviyte

class Editbacsi(ModelForm):
    class Meta:
        model = Bacsi
        fields = 'ten','address','gioitinh','ngaysinh','tinhthanh','quanhuyen','xaphuong','donviyte'


class u_r(ModelForm):
    class Meta:
        model=User
        fields='username','password','email','phone','motacongviec'

class dvytf(ModelForm):
    class Meta:
        model=Donviyte
        fields = 'ten','diachi','trangthaidonvi','quanhuyen','xaphuong','tinhthanh'
