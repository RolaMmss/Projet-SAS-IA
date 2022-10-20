from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignupPage(CreateView):
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'
    



# Create your views here.

# def signup_create(request):
#     if request.method =="POST" :
#         form = forms.UserForm(request.POST)
#         if form.is_valid() :
#             user = form.save()
   
#             # return redirect(request, ' /home', context = {'form' : form})
#     else :
#         form = forms.UserForm()
#     return render(request,
#             'signup/signup_page.html',
#             {'form': form})




