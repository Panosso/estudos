from django.db import models


#Toda classe criada nesse passo é necessário herdar de models.Model para poder aparecer e ser usada no /admin
# após a criação da classe é necessário rodar o makemigrations e migrate no manage.py para poder funcionar as classes
# no admin.py da aplicação é necessário alterações tbm.
class CPF(models.Model):
    numero = models.CharField(max_length=14)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Empregado(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=1000, blank=False, null=False)
    idade = models.IntegerField(blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, null=True, blank=True)
    departamento = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to='cliente_foto')


    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=1000)
    cliente = models.ForeignKey(Empregado)

    def __str__(self):
        return f'{self.numero} - {self.descricao}'
