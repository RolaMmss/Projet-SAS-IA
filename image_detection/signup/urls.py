from django.urls import path
from . import views

app_name = "signup"

urlpatterns = [
    path('', views.SignupPage.as_view()),
    # path('', views.signup_create),
    
]
