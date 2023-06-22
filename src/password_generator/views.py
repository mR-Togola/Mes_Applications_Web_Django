from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.




def password_generator(request):
    liste  = ['4','5','6','7','8','9','10','11','12', '13']
    return render(request, 'password/index.html', context={'mdp': 'OKOK', 'listes':liste} )



def mdp(request):
    
    caracteres = list(string.ascii_lowercase)
    longueur = int(request.GET.get('longueur'))
    
    if request.GET.get('majuscule'):
        caracteres.extend(list(string.ascii_uppercase))
    
    if request.GET.get('special'):
        caracteres.extend(list('&ê@à#*£$ûâ_-."'))
    
    if request.GET.get('nombres'):
        caracteres.extend(list('0123456789'))
        
    print(caracteres)
    mdp = ''
    for x in range(longueur):
        mdp += random.choice(caracteres)
    
    print(caracteres)
    return render(request, 'password/password_genered.html',{'mdp': mdp} )
