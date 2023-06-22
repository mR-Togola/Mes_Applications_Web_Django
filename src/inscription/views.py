#from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from inscription.forms import Formulairedeparticipant


def actuel():
    maintenant = datetime.now().hour
    heure = datetime.today()
    if maintenant < 12:
        actu = "Bonjour"
    else:
        actu = "Bonsoir"
    return actu, heure


def index(request):
     actu,heure = actuel()
     context = {
        "actu": actu,
        "heure":heure
     }
     date = datetime.today()
     return render(request, "index.html", context)



def formulaire(request):
    submitted = False
    form = Formulairedeparticipant
    if request.method == "POST":
        form = Formulairedeparticipant(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Formulairedeparticipant
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "signup.html", {"form":form} )





