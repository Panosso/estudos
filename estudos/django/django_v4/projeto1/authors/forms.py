import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


def strong_passwd(password):
    regex = re.compile(r"(?=.*[a-z])")

    if not regex.match(password):
        raise ValidationError(
            (
                "Password must have at least one uppercase letter, "
                "one lowercase letter and one number. The length should be "
                "at least 8 characters."
            ),
            code="invalid",
        )


class RegisterForm(forms.ModelForm):
    # Só de colocar uma validação nesse arquivo
    # o django vai passar e validar
    # o que precisar, como passwd, email e afins
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["username"], "Your username")
        add_placeholder(self.fields["email"], "Your e-mail")
        add_placeholder(self.fields["first_name"], "Ex.: John")
        add_placeholder(self.fields["last_name"], "Ex.: Doe")
        add_attr(self.fields["username"], "css", "a-css-class")

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Your password"}),
        error_messages={"required": "Password must not be empty"},
        help_text=(
            "Password must have at least one uppercase letter, "
            "one lowercase letter and one number. The length should be "
            "at least 8 characters."
        ),
        validators=[strong_passwd],
    )

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

        # Todos os campos podem ser validados com o
        # clean_<nome_do_campo>
        def clean_email(self):
            email = self.cleaned_data.get("email", "")
            existe = User.objects.filter(email=email).exists()

            if existe:
                raise ValidationError("Ja está sendo usado", code="invalid")

            return email

        def clean_password(self):
            # self.data retorna o valor do campo cru, ou seja,
            # retorna o valor do jeito que ele vem do form

            # self.cleaned_data retorna um dicionário, e nele
            # podemos pegar o valor atraves do get
            # e esse valor ja vem limpo pra gente.
            data = self.cleaned_data.get("password")

            # Exemplo de uma validação
            if "atencao" in data:
                raise ValidationError(
                    "Não digite %(value)s na senha",
                    code="Inválido, presta mais atencao",
                    params={"value": "atenção"},
                )

            return data

        def clean(self):
            # Quando chamamos o super da classe
            # podemos acessar o metodo clean
            # que traz os campos do formulário
            # limpos, ou seja, sem html nem nada
            # apenas o valor dele
            clean_data = super().clean()
            passwd = clean_data.get("password")
            passwd2 = clean_data.get("password2")

            if passwd != passwd2:
                raise ValidationError(
                    {
                        "password": ValidationError(
                            "Password and password2 tem que ser igual",
                            code="invalid",  # noqa: 501
                        ),
                        "password2": [
                            ValidationError(
                                "Password and password2 tem que ser igual 1"
                            )
                        ],
                    }
                )  # noqa: 501
