from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *

# Create your views here.

def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('Data Is Not Valid')
    
    return render(request,'student.html',d)