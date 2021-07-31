from django.db import models
from user.models import User,Donviyte,Bacsi
from location.models import Tinhthanh,Quanhuyen,Xaphuong
# Create your models here.
class Benhnhan(models.Model):
    ten=models.CharField(max_length=50)
    sex_choice=(('1','Nam'), ('0','Nữ'))
    sex=models.CharField(max_length=10, choices=sex_choice, default='')
    ngaysinh=models.DateField()
    phone=models.CharField(default='',max_length=15)
    email=models.CharField(default='',max_length=100)
    mabaohiem=models.CharField(default='',max_length=15)
    bhyt_ngaycap=models.DateField()
    bhyt_sudungtu=models.DateField()
    bhyt_sudungden=models.DateField()
    macongdan=models.CharField(default='',max_length=15)
    nguoilienhe=models.CharField(max_length=255)
    sdt_nguoilienhe=models.CharField(default='',max_length=15)
    donviyte=models.ForeignKey(Donviyte, on_delete=models.CASCADE)
    tinhthanh=models.ForeignKey(Tinhthanh, on_delete=models.CASCADE)
    quanhuyen=models.ForeignKey(Quanhuyen, on_delete=models.CASCADE)
    xaphuong=models.ForeignKey(Xaphuong, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten


class Quanlybenhnhan(models.Model):
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    benhnhan_id=models.ForeignKey(Benhnhan, on_delete=models.CASCADE)
    bacsi_id=models.ForeignKey(Bacsi, on_delete=models.CASCADE)