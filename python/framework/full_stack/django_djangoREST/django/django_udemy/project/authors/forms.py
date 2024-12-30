from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.django_forms import strong_password

class RegisterForm(forms.ModelForm):
    
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': "Digite a senha ae e que seja FORTE!!!"
        })
    )

    password = forms.CharField(
        validators=[strong_password]
    )

    #Classe para informar metadados
    class Meta:
        model = User

        #Retorna todos os fields do models.py da class User
        # fields = '__all__'

        #Retornar apenas alguns campos
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

        #Muda os nomes dos labels.
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }

        #Muda o help text do campo
        help_text = {
            'email': 'Email precisa ser válido',
        }

        #Editando os erros, e cada elemento pode conter mais de um erro
        error_messages = {
            'username' : {
                'required': 'Precisa preencher esse campo amigo',
                'max_lenght': 'Precisa ter pelo menos de 3 caracteres'
            }
        }

        #Editando os widgets
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': "Digite seu username, mas não inventa"
            }),
            'password': forms.TextInput(attrs={
                'placeholder': 'Digite uma senha FORTE'
            })
        }


    #Validando o campo após a palavra 'clean_'
    #Nesse exemplo, esse metodo sera chamado quando o campo 'password' for utilizado
    def clean_password(self):
        #Os dados vem do jeito mais cru possível
        # data = self.data

        #Aqui os dados estão tratatos
        data = self.cleaned_data.get('password')
        print(data)
        
        if '123' in data:
            raise ValidationError(
                'Não digite %(valor)s no campo senha, animal',
                code='invalid',
                params={'valor': '"123"'}
            )

        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exists()

        if exist:
            raise ValidationError(
                'Esse e-mail ja está sendo usado!',
                code='invalid',
            )

    #Esse método é chamado após todos os métodos clean_* serem executados
    def clean(self):
        cleaned_data = super().clean()

        passwd = cleaned_data.get('password')
        passwd2 = cleaned_data.get('password2')

        if passwd != passwd2:
            raise ValidationError(
                {'password': 'Pass1 e Pass2 tem que ser igual, ZÉ!!!'}
            )
        
#Apenas para criar um formulario
class LoginsForm(forms.Form):
    
    username = forms.CharField(
        widget=forms.TextInput({
            'placeholder': "Digite seu username, mas não inventa"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput({
            'placeholder': "Digite sua senha"
            })
    )
