from django import forms
from .models import Destination

class DestinosTuristicosForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name','img', 'desc',  'price', 'offer']
