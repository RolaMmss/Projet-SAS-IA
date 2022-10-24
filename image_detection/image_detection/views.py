from django.shortcuts import render


def homepage(request):
    context = {
    }

    return render (request, "home_page.html", context = context)