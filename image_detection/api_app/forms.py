from django.shortcuts import render
from . import forms
import json

def api (request):
    url = "https://api.everypixel.com/v1"