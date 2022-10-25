from django import forms
from . import models
from django.forms import CheckboxSelectMultiple

class ApiForm(forms.ModelForm):
    class Meta:
        model = models.ApiModel
        fields = "__all__"
        labels = {
            "url": "Entrez l'url de votre image",
            # "num_keywords": "Entrez le nombre max de mots-clés"
        }
        # widgets = {
        #     "api_choices":CheckboxSelectMultiple()
        # }
