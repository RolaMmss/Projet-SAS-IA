from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def signup_create(request):
    if request.method =="POST" :
        form = forms.UserForm(request.POST)
        if form.is_valid() :
            user = form.save()
   
            # return redirect(request, ' /home', context = {'form' : form})
    else :
        form = forms.UserForm()
    return render(request,
            'signup/signup_page.html',
            {'form': form})




