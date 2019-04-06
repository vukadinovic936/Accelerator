# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import HomeForm
from django.shortcuts import render,render_to_response

# Create your views here.
def index(request):
    template_name=('index.html')
    form=HomeForm()
    form.fields['post'].label = "Email"
    if request.method=="GET":
        return render(request,'index.html',{'form':form})
    if request.method=="POST":
        form= HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form=HomeForm()
            handle=open('emails.txt','r+')
            var=handle.read()
            var+=text
            var+=';'
            handle1=open('emails.txt','r+')
            handle1.write(var)
            handle1.close()
            text="Thanks for signing up!"
        args= {'form': form, 'text': text}
        return render(request, template_name,args)
