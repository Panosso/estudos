from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    
    #Classe para informar metadados
    class Meta:
        model = User

        #Retorna todos os fields do models.py da class User
        # fields = '__all__'

        #Retornar apenas alguns campos
        fields = [
            'first_name',
            'last_name'
        ]


