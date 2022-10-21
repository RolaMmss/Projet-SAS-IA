from django import forms
from . import models


class ApiKeywordsForm(forms.ModelForm):
    class Meta:
        model = models.ApiKeywordsModel
        fields = "__all__"
        labels = {
            "url": "Entrez l'url de votre image",
            "num_keywords": "Entrez le nombre max de mots-clés"
        }
