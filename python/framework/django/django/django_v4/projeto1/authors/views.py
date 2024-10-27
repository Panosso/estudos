from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


# Create your views here.
def register_view(request):
    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    return render(
        request,
        "authors/templates/author/pages/register_view.html",
        {
            "form": form,
        },
    )


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        # Com esse commit eu não salvo o form direto
        # podendo altera-lo caso necessário.
        # data = form.save(commit=False)
        # data._outrocampo = 'Alguma coisa'
        # data.save()

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Criado com sucesso.")
        del request.session["register_form_data"]
        return redirect(reverse("authors:login"))

    return redirect("authors:register")


def login_view(request):
    form = LoginForm()

    return render(
        request, "authors/templates/author/pages/login.html", {"form": form}
    )  # noqa: E501


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse("authors:login_create")

    if form.is_valid():
        is_autenticated = authenticate(
            username=form.cleaned_data.get("username", ""),
            password=form.cleaned_data.get("password", ""),
        )

        if is_autenticated is not None:
            messages.success(request, "Usuário conectado")
            login(is_autenticated)
        else:
            messages.error(request, "Credenciais inválidas")
    else:
        messages.error(request, "Formulario invalido")

    return redirect(login_url)
