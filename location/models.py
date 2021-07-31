from django.db import models

# Create your models here.
class Tinhthanh(models.Model):
    matinhthanh=models.CharField(max_length=10)
    tentinhthanh=models.CharField(max_length=100)
    def __str__(self):
        return self.tentinhthanh

class Quanhuyen(models.Model):
    maquanhuyen=models.CharField(max_length=10)
    tenquanhuyen=models.CharField(max_length=100)
    tinhthanh=models.ForeignKey(Tinhthanh, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.tenquanhuyen

class Xaphuong(models.Model):
    maxaphuong = models.CharField(max_length=10)
    tenxaphuong = models.CharField(max_length=100)
    quanhuyen = models.ForeignKey(Quanhuyen, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.tenxaphuong