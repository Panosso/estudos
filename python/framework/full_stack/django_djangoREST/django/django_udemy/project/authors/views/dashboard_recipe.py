from django.http.response import Http404
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import connection
from authors.forms import AuthorRecipeForm
from recipes.models import Recipe


@method_decorator(
        login_required(login_url='authors:login', redirect_field_name='next'),
        #Colocando esse código, o método dispatch (que é o responsável por ser um handler entre request e response) será decorado com esse login required
        name='dispatch'
)
class DashboardRecibe(View):

    def get_recipe(self, id_receita=None):
        
        recipe = None

        if id_receita is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id_receita,
            ).first()

            if not recipe:
                raise Http404
        
        return recipe

    def render_recipe(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_recipe.html',
            context={
                'form': form
            }
        )

    def get(self, request, id_receita=None):

        recipe = self.get_recipe(id_receita) if id_receita else None

        form = AuthorRecipeForm(instance=recipe)

        return self.render_recipe(form)

    def post(self, request, id_receita=None):

        recipe = self.get_recipe(id_receita)

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

            return redirect(reverse('authors:dashboard_recipe_edit', args=(recipe.id,)))

        return self.render_recipe(form)


#não é necessário colocar esse decorator, porém é interessante reforçar o sistema.
@method_decorator(
        login_required(login_url='authors:login', redirect_field_name='next'),
        #Colocando esse código, o método dispatch (que é o responsável por ser um handler entre request e response) será decorado com esse login required
        name='dispatch'
)
class DashboardRecibeDelete(DashboardRecibe):
    def post(self, *args, **kwargs):
        recipe = self.get_recipe(self.request.POST.get('id'))
        recipe.delete()
        messages.success(self.request, 'receita deletada')
        return redirect(reverse('authors:dashboard'))