from django.shortcuts import render,redirect
from django.contrib.auth import login
from .form import BacsiSignUpForm,Editbacsi,u_r,DonviyteSignupForm,dvytf
from django.views.generic import CreateView
from .models import User,Bacsi
from django.views import View
from .models import Donviyte
from .filters import DonviyteFilter,BacsiFilter,UserFilter



class BacsiSignUpView(CreateView):
    model = User
    form_class = BacsiSignUpForm
    template_name = 'signup/registerpersonnel.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'bacsi'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('core:login')

class DonviyteSignUpView(CreateView):
    model = User
    form_class = DonviyteSignupForm
    template_name = 'signup/dangkidonviyte.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'donviyte'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        return redirect('user:donviyteview')

class Editprofile(View):
    def get(self,request):
        bs=Bacsi.objects.get(user__id=request.user.id)
        form=Editbacsi(instance=bs)
        ur=User.objects.get(id=request.user.id)
        form1=u_r(instance=ur)
        context={'bs':form,'ur':form1}
        return render(request,'templates/edit-profile.html',context)
    def post(self,request):
        bs=Bacsi.objects.get(user__id=request.user.id)
        if request.method=='POST':
            form=Editbacsi(request.POST,instance=bs)
            if form.is_valid():
                form.save()
                phone=request.POST['phone']
                email=request.POST['email']
                motacongviec=request.POST['motacongviec']
                ur=User.objects.get(id=request.user.id)
                ur.phone=phone
                ur.email=email
                ur.motacongviec=motacongviec
                ur.save()
                return redirect('user:editprofile')
            return redirect('user:editprofile')

class Editprofiledvyt(View):
    def get(self,request):
        dvyt=Donviyte.objects.get(user__id=request.user.id)
        form=dvytf(instance=dvyt)
        ur=User.objects.get(id=request.user.id)
        form1=u_r(instance=ur)
        context={'dvyt':form,'ur':form1}
        return render(request,'donviyte/edit-dvyt.html',context)
    def post(self,request):
        dvyt=Donviyte.objects.get(user__id=request.user.id)
        if request.method=='POST':
            form=dvytf(request.POST,instance=dvyt)
            if form.is_valid():
                form.save()
                phone=request.POST['phone']
                email=request.POST['email']
                motacongviec=request.POST['motacongviec']
                ur=User.objects.get(id=request.user.id)
                ur.phone=phone
                ur.email=email
                ur.motacongviec=motacongviec
                ur.save()
                return redirect('user:donviyteedit')

def donviyte(request):
    dv=Donviyte.objects.all()
    myfilter=DonviyteFilter(request.GET,queryset=dv)
    dv=myfilter.qs

    context = {"dv": dv,'myfilter':myfilter}

    return render(request,'donviyte/donviyte.html',context)

def bacsi(request):
    bs=Bacsi.objects.all()
    myfilter = BacsiFilter(request.GET, queryset=bs)
    bs = myfilter.qs
    return render(request,'bacsi/bacsi.html',{'bs':bs,'myfilter':myfilter})

# def user(request):
#     user=User.objects.all()
#     muser = UserFilter(request.GET,queryset=user)
#     user=muser.qs
#     return render(request,'donviyte/donviyte.html',{'muser':muser})



