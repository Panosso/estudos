from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Verifica se o usuario pode autenticar e o login dele, criando sessão cookie e afins
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm, LoginsForm

# Create your views here.
def register_view(request):

    register_form_data = request.session.get('register_form_data', None)

    form_view = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html', {'form': form_view})

def register_create(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form_view = RegisterForm(request.POST)

    if form_view.is_valid():
        user = form_view.save(commit=False)
        print(dir(user))
        user.set_password(user.password)
        user.save()
        #Essa mensagem é como se fosse uma variavel do Django, portanto ela não precisa ser passada como parametro.
        #Quando o Django carrega a página ele verifica se tem mensagem e se tiver exibe
        messages.success(request, 'Foi cadastrado com sucesso')
        del(request.session['register_form_data'])


    return redirect('authors:register')

def login_view(request):

    form_view = LoginsForm()

    return render(request, 'authors/pages/login.html', {
                    'form': form_view,
                    'form_action': reverse('authors:login_create')
                    })

def login_create(request):
    
    if not request.POST:
        raise Http404()

    form = LoginsForm(request.POST)
    login_url = reverse('authors:login')

    if form.is_valid():
        authenticate_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            messages.success(request, 'Usuário logado!!!')
            login(request, user=authenticate_user)

        else:
            messages.error(request, 'Credenciais invalidas!!!')
    
    else:

        messages.error(request, 'Error to validate form data')
    
    return redirect(login_url)

#Avisa o Django que para acessar essa view o usuario precisa estar logado
#Esse next envia o usuario para onde ele tentou acessar sem estar logado.
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    logout(request)

    return redirect(reverse('authors:login'))