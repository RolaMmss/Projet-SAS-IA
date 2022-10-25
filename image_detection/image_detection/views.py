from django.shortcuts import render


def homepage(request):
    context = {
    }

    return render (request, "home_page.html", context = context)



def services(request):
    context = {
    }

    return render (request, "services.html", context = context)

def sign_in(request):
    context = {
    }

    return render (request, "signin.html", context = context)

def sign_up(request):
    context = {
    }

    return render (request, "signup.html", context = context)