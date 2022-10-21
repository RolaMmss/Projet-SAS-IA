from urllib import response
from django.shortcuts import render
from . import forms
import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')



def api_keywords(request):
        url_api="https://api.everypixel.com/v1/keywords"

        if request.method =="POST":
                form = forms.ApiKeywordsForm(request.POST)
                if form.is_valid():
                    # param = {"url": form.url, "num_keywords":form.num_keywords}
                    print(form.cleaned_data)
                    reponse = requests.get(url_api, params = form.cleaned_data, auth =(CLIENT_ID,CLIENT_SECRET))
                    form.save()
                    info = json.loads(reponse.text)
                    print(info)
                    return render(request, 'api_app/reponse_formulaire.html', context = {'form' : form, 'info' :info})

        else :
            form = forms.ApiKeywordsForm()
        return render(request, 'api_app/formulaire.html', context = {'form' : form})







        
        



