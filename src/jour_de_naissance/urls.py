from django.urls import path
from .views import jour_d_naissance

app_name = "naissance"

urlpatterns = [

    path('',jour_d_naissance, name='jour' ),
    path('days/', jour_d_naissance, name='find_birth_day')
   
    #path(),

]