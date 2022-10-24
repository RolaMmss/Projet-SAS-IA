from django.urls import path
from . import views


app_name = "signup"

urlpatterns = [
    path('', views.SignupPage.as_view(), name='sign_up'),
    # path('', views.signup_create),
    
]
