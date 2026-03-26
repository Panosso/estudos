from django.db import models

# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=255)

    #Para evitar a dupla importação de User, utilizamos a string "accounts.User" para referenciar o modelo de usuário criado na app accounts
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='enterprises')

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='employee_profiles')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='employees')

    def __str__(self) -> str:
        return self.name 