from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
def Xaphuong(request):
    return render(request,'danhmuc/xaphuong.html')
def Quanhuyen(request):
    return render(request,'danhmuc/quanhuyen.html')
def Tinhthanh(request):
    return render(request,'danhmuc/tinhthanh.html')