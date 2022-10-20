from django.shortcuts import render
from . import forms
from requests import Session
import json
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

def api(request):
        url="https://api.everypixel.com/v1"
