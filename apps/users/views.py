# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users
from .forms import UserForm
from django.utils import timezone


def index (request) :
    
    
    context = {'users': Users.objects.all()
              }
    print context
    return render(request, 'users/index.html', context)

def edit (request, userId) :
    print "in edit, id: ",userId
    
    if int(userId) != 0:
        print "edit mode"
        user = Users.objects.get(pk=userId)
        print "user: ", user
        data = {'first_name': user.first_name, 'last_name': user.last_name, 'email_address': user.email_address}
        form = UserForm(initial = data)
        addEdit = "Update"
    else:
        print "add mode"
        form = UserForm()
        addEdit = "Add"
    
    context = {'form' : form,
                'addEdit': addEdit,
                'id': userId}

    return render(request, 'users/addEdit.html', context)
 
def delete (request, userId) :
    print "in delete, id: ", userId
    user = Users.objects.get(pk=userId)
    print user
    user.delete()
    return redirect(reverse('users:home'),kwargs={'id': 0 })
    
def addEdit(request, userId) :
    

    if request.method == "POST" :
        print "in addEdit, request.POST: ", request.POST
        if ("Add" in request.POST):
            # Add new record
            Users.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email_address = request.POST["email_address"], created_at = timezone.now())
        else :
            user = Users.objects.get(pk=userId)
            print user
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.email_address = request.POST["email_address"]
            user.updated_at = timezone.now()
            user.save()

    return redirect(reverse('users:home'))