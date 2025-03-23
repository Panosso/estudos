from django.db import models

# Create your models here.
class Person(models.Model):

    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nascimento = models.DateField(auto_now=False,null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    altura = models.FloatField(null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    peso_ideal = models.FloatField(null=False, blank=False)


    def __str__(self):
        return self.nome
    
    def calc_peso_ideal(self, sexo, altura):

        peso_ideal = 0

        if sexo == "M":

            peso_ideal = (72.7 * altura) - 58

        else:

            peso_ideal = (62.1 * altura) - 44.7

        return peso_ideal

    def save(self, *args, **kwargs):

        self.peso_ideal = self.calc_peso_ideal(self.sexo, self.altura)

        saved = super().save(*args, **kwargs)

        return saved
