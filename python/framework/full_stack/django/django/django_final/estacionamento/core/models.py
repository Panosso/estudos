from django.db import models
import math

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(null=False, max_length=100, blank=False)
    sobrenome = models.CharField(max_length=200, blank=False)
    endereco = models.CharField(max_length=200, blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Categoria(models.Model):
    categoria = models.CharField(max_length=2, blank=False)
    descricao = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.categoria

class Marca(models.Model):
    marca = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.marca}'

class Cor(models.Model):
    cor = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{self.cor}'

class Veiculo(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    observacao = models.TextField()
    proprietario = models.ForeignKey('Pessoa', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.placa} - {self.marca}'

class MovRotativoHora(models.Model):

    entrada = models.DateTimeField(auto_now=False)
    saida = models.DateTimeField(auto_now=False, null=True, blank=True)
    vl_hora = models.ForeignKey('Parametros', on_delete=models.CASCADE)
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        #Função do Django que retorna a diferença de datas em segundos
        return math.ceil((self.saida - self.entrada).total_seconds() / 3600)

    def total(self):
        #Pelo relacionamento é possível acessar o parametro valor_hora
        return self.vl_hora.valor_hora * self.horas_total()

    def __str__(self):
        if self.pago == True:
            self.pago = 'Pago'
        else:
            self.pago = 'Não Pago'
        return f'{self.veiculo.placa} - {self.veiculo.proprietario.nome} - {self.pago}'

class MovMensalista(models.Model):
    mensalista = models.ForeignKey('MovRotativoMes', on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.mensalista} - {self.total}'

class MovRotativoMes(models.Model):

    entrada = models.DateField(auto_now=False)
    saida = models.DateField(auto_now=False, null=True, blank=True)
    vl_mes = models.ForeignKey('Parametros', on_delete=models.CASCADE)
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def __str__(self):
        if self.pago == True:
            self.pago = 'Pago'
        else:
            self.pago = 'Não Pago'
        return f'{self.veiculo.placa} - {self.veiculo.proprietario} - {self.pago}'

class Parametros(models.Model):
    valor_hora = models.DecimalField(verbose_name='Valor por hora', max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(verbose_name='Valor por mes', max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Parametros gerais'
