from django.shortcuts import render
from datetime import datetime


def jour_d_naissance(request):
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        try:
            parsed_date = datetime.strptime(birth_date, "%d/%m/%Y")
            jour_naissance = parsed_date.weekday()
            jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
            #birth_day = parsed_date.strftime('%A')
            return render(request, 'jours/result.html', {'birth_day': jours[jour_naissance]})
        except ValueError:
            error_message = 'Format de date non valide. Veuillez saisir la date au format JJ/MM/AAAA'
            return render(request, 'jours/jours.html', {'error_message': error_message})
    else:
        return render(request, 'jours/jours.html')
    
    
