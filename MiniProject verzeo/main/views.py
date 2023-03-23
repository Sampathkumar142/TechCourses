from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserQueryForm


# Create your views here.



def getHome(request):
    return HttpResponse(render(request,'base/home.html'))

    
def about(request):
    return HttpResponse(render(request,'base/about.html'))






def UserQueryForm(request):
    if request.POST:
        if request.POST.get('email') and request.POST.get('message'):
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(email)
            print(message)
            models.UserQuery.objects.create(email=email,message = message)
        return HttpResponse(render(request,'base/contact.html'))
    else:
        return render(request,'base/contact.html')


def courses(request):
    result = models.Courses.objects.values()             
    list_result = [entry for entry in result]
    return HttpResponse(render(request,'base/courses.html',{'dict':list_result}))