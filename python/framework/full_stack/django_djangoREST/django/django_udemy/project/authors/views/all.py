from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Verifica se o usuario pode autenticar e o login dele, criando sessão cookie e afins
from django.contrib.auth import authenticate, login, logout

from authors.forms import RegisterForm, LoginsForm, AuthorRecipeForm
from recipes.models import Recipe

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
    
    return redirect(reverse('authors:dashboard'))

#Avisa o Django que para acessar essa view o usuario precisa estar logado
#Esse next envia o usuario para onde ele tentou acessar sem estar logado.
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    logout(request)

    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):

    recipes = Recipe.objects.filter(
        is_published=False,
        author = request.user
    )

    return render(request, 
                  'authors/pages/dashboard.html',
                  context={
                      'recipes': recipes
                  })

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_edit(request, id_receita):
    recipe = Recipe.objects.filter(
        is_published=False,
        author=request.user,
        pk=id_receita,
    ).first()

    if not recipe:
        raise Http404()

    form = AuthorRecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )

    if form.is_valid():
        recipe = form.save(commit=False)

        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_publish = False

        recipe.save()

        messages.success(request, 'Sua receita foi salva com sucesso.')

        return redirect(reverse('authors:dashboard_recipe_edit', args=(id,)))

    return render(
        request,
        'authors/pages/dashboard_recipe.html',
        context={
            'form': form
        }
    )

@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_new(request):
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        recipe: Recipe = form.save(commit=False)

        recipe.author = request.user
        recipe.preparation_steps_is_html = False
        recipe.is_published = False

        recipe.save()

        messages.success(request, 'Salvo com sucesso!')
        return redirect(
            reverse('authors:dashboard_recipe_edit', args=(recipe.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_recipe.html',
        context={
            'form': form,
            'form_action': reverse('authors:dashboard_recipe_new')
        }
    )