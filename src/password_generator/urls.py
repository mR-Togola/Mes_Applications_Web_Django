from django.urls import path
from .views import password_generator, mdp

app_name = "password"

urlpatterns = [

    path('',password_generator, name='password_generator' ),
    path('mot_de_passe_generer/',mdp, name='mdp')
    #path(),

]