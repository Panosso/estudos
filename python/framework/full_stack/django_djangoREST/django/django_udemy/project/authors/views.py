from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.
def register_view(request):

    form_view = RegisterForm()

    return render(request, 'authors/pages/register_view.html', {'form_view': form_view})
