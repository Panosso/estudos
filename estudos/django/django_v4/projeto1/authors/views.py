from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


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

    return redirect("authors:register")
