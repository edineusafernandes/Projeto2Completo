from django.db import models

# Create your models here.
class User (models.Model):
    nome = models.CharField('nome', max_length=30)
    telefone = models.BigIntegerField('telefone')
    email = models.CharField('email', max_length=30)

    def _str_(self):
        return f"Nome:  {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}"
