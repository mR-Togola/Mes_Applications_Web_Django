from django.db import models



class ParticipantForm(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    


    class Meta:
        verbose_name = "Participant"

    def __str__(self) :
        return self.nom
        

    def get_absolute_url(self):
        return 'https://www.google.fr'


