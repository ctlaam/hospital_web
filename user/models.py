from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from location.models import Tinhthanh,Xaphuong,Quanhuyen

class User(AbstractUser):
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        phone = models.CharField(max_length=15, null=True)
        motacongviec = models.CharField(max_length=255)
        is_benhnhan = models.BooleanField(default=False)
        is_bacsi = models.BooleanField(default=False)
        is_donviyte = models.BooleanField(default=False)
        is_admin = models.BooleanField(default=False)
class Donviyte(models.Model):
    ten = models.CharField(max_length=50,null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    diachi=models.CharField(max_length=100)
    trangthai = (('Hoạt động', 'Hoạt động'), ('Không hoạt động', 'Không hoạt động'))
    trangthaidonvi=models.CharField(max_length=20 ,choices=trangthai,default='',null=True)
    tinhthanh=models.ForeignKey(Tinhthanh, on_delete=models.CASCADE,null=True)
    quanhuyen=models.ForeignKey(Quanhuyen, on_delete=models.CASCADE,null=True)
    xaphuong=models.ForeignKey(Xaphuong, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.ten

class Bacsi(models.Model):
    ten = models.CharField(max_length=50, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    sex_choice = (('1', 'Nam'), ('0', 'Nữ'))
    address=models.CharField(max_length=200)
    gioitinh = models.CharField(max_length=10, choices=sex_choice, default='', null=True)
    ngaysinh=models.DateField(null=True)
    donviyte=models.ForeignKey(Donviyte, on_delete=models.CASCADE, null=True)
    tinhthanh=models.ForeignKey(Tinhthanh, on_delete=models.CASCADE, null=True)
    quanhuyen=models.ForeignKey(Quanhuyen, on_delete=models.CASCADE, null=True)
    xaphuong=models.ForeignKey(Xaphuong, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.ten

