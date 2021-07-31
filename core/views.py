from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Index(LoginRequiredMixin,View):

    login_url = 'core:login'
    def get(self, request):
        return render(request,'templates/home.html')

class Login(View):
    def get(self,request):
        return render(request,'templates/login.html')

class Logout(View):
     def get(self, request):
        return render(request,'templates/login.html')

     def post(self, request):
         user_name = request.POST.get('tendangnhap')
         pass_word = request.POST.get('matkhau')
         my_user = authenticate(username=user_name, password=pass_word)
         if my_user is None:
             return HttpResponse('Sai tài khoản hoặc tên đăng nhập')
         login(request, my_user)
         return redirect('core:index')


class Dangki(View):
    def get(self,request):
         return render(request,'signup/dangki.html')
