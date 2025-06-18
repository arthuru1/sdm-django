from django import forms
from .models import SDM

class SDMForm(forms.ModelForm):
    class Meta:
        model = SDM
        fields = ['nama', 'alamat', 'jabatan']
