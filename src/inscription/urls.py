from django.urls import path
from inscription.views import index, formulaire



urlpatterns = [
    path('', index, name="blog-index"),
    path('inscription/',formulaire, name="inscription"),
   
]