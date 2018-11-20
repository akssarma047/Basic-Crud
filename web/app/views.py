from django.shortcuts import render,HttpResponse,redirect
from .models import *


def index(request):
    members = Members.objects.all()
    gh = {'members': members}
    return render(request, 'index.html', gh)


def create(request):
    member = Members(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')


def edit(request, id):
    members = Members.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)

def update(request, id):
    member = Members.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/')

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect('/')
# Create your views here.
