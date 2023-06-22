from django.forms import ModelForm
from inscription.models import ParticipantForm


class Formulairedeparticipant(ModelForm):
    class Meta:
        model = ParticipantForm
        fields = ('nom', 'prenom', 'telephone','email', )