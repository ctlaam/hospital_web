from django.shortcuts import render,redirect
from django.views import View
from .models import Benhnhan
from .forms import BenhnhanForm
from .filters import BenhnhanFilter

# Create your views here.
def Patient(request):
    benhnhan = Benhnhan.objects.all()
    myfilter=BenhnhanFilter(request.GET,queryset=benhnhan)
    benhnhan=myfilter.qs
    context = {"bn": benhnhan, 'myfilter':myfilter}

    return render(request, "patient/patients.html", context)


def Thembenhnhan(request):
    form = BenhnhanForm()
    if request.method == 'POST':
        form=BenhnhanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient:benhnhan')
    context={'form':form}
    return render(request, 'patient/add-patient.html', context)


def Updatebenhnhan(request,pk):
    benhnhan=Benhnhan.objects.get(id=pk)
    form = BenhnhanForm(instance=benhnhan)
    if request.method == 'POST':
        form=BenhnhanForm(request.POST,instance=benhnhan)
        if form.is_valid():
            form.save()
            return redirect('patient:benhnhan')
    context={'form':form}
    return render(request, 'patient/add-patient.html', context)

def Deletecbenhnhan(request,pk):
    benhnhan = Benhnhan.objects.get(id=pk)
    if request.method == 'POST':
        benhnhan.delete()
        return redirect('patient:benhnhan')
    context = {'benhnhan':benhnhan}
    return render(request,'patient/delete-patient.html',context)

def deletecauhoi(request,pk):
    question = Question.objects.get(id=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('polls:view_list')
    context = {'item':question}
    return render(request,'polls/delete.html',context)

