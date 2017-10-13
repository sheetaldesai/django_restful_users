# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Users
from .forms import UserForm
from django.utils import timezone


def index (request, id) :
    print "id: ",id
    if (id) :
        user = User.objects.get(pk=id)
        print "user: ", user
        form = UserForm(user)
        addEdit = "Update"
    else:
        form = UserForm()
        addEdit = "Add"
    context = {'users': Users.objects.all(),
                'form' : form,
                'addEdit' : addEdit}
    print context
    return render(request, 'users/index.html', context)

def edit (request, userId) :
    print "in edit, id: ",userId
    return redirect(reverse('users:home'),kwargs={'id': userId })

def delete (request, userId) :
    print "in delete, id: ", userId
    user = Users.objects.get(pk=userId)
    print user
    user.delete()
    return redirect(reverse('users:home'),kwargs={'id': 0 })
    
def addEdit(request) :
    
    if request.method == "POST" :
        print "in addEdit, request.POST: ", request.POST
        if ("Add" in request.POST):
            # Add new record
            Users.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email_address = request.POST["email_address"], created_at = timezone.now())

    return redirect(reverse('users:home'),kwargs={'id': 0 })