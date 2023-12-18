from django.forms import ModelForm
from .models import (Pessoa,
                     Veiculo,
                     MovRotativoHora,
                     MovRotativoMes,
                     Categoria,
                     Cor,
                     Marca,
                     Parametros)

#Criado os forms que utilizamos no cadastro em suas respectivas paginas html
# as classes precisam dessa sebclasse 'Meta', pois nela que conseguimos pegar
# os tipos dos fields criados no model.

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MovRotHoraForm(ModelForm):
    class Meta:
        model = MovRotativoHora
        fields = '__all__'

class MovRotMesForm(ModelForm):
    class Meta:
        model = MovRotativoMes
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CorForm(ModelForm):
    class Meta:
        model = Cor
        fields = "__all__"

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class ParametrosForm(ModelForm):
    class Meta:
        model = Parametros
        fields = "__all__"
