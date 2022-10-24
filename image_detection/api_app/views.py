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



def api(request):
        url_api="https://api.everypixel.com/v1/faces"

        if request.method =="POST":
                form = forms.ApiForm(request.POST)
                if form.is_valid():
                    # param = {"url": form.url, "num_keywords":form.num_keywords}
                    print(form.cleaned_data)
                    reponse = requests.get(url_api, params = form.cleaned_data, auth =(CLIENT_ID,CLIENT_SECRET))
                    form.save()
                    info = json.loads(reponse.text)["faces"][0]
                    print(info)
                    return render(request, 'api_app/reponse_formulaire.html', context = {'form' : form, 'age' : info["age"] , 'score': info["score"], 'class':info['class']})

        else :
            form = forms.ApiForm()
        return render(request, 'api_app/formulaire.html', context = {'form' : form})











        
        



