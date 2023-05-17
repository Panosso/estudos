from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_val):
    existing_attr = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_val}".strip()


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_attr(self.fields["username"], "placeholder", "Digite seu username")

    # Podemos criar campos apenas para o formulário
    # que não estejam no model,
    # podemos tambem podemos sobreescrever um campo
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Digite novamente seu passwd"}
        ),
    )

    # Classe que passa metadados para o formulario
    class Meta:
        model = User
        # Se colocar '__all__' é possível editar todos os campos do model
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

        # No momento que o form é montado, ele vai pedir
        # todos os campos EXCETO os mencionados nesse variavel.
        # exclude = ['first_name']

        # Podemos definir o nome do label do form
        # nesse exemplo o campo username,
        # vai aparecer como 'Digite seu usuario'
        labels = {"username": "Digite seu usuario"}

        # Podemos definir o help_text
        # assim o que digitar aqui é o que vai aparecer no form
        help_text = {"email": "Digite um email e tem que ter um @"}

        # Podemos definir o campo ser requerido invalido ou
        # outras propriedades de um form
        error_messages = {
            "username": {"required": "Esse campo precisa ser preenchido <3"}
        }

        # Podemos reescrever o widget do campo
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Digite o seu nome aqui",
                    "class": "input text-input outra-classe",
                }
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Digita o passwd aqui"}
            ),
        }
