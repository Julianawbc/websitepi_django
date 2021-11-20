from django.db import models  #os models recebe o banco de dados criado no runserver admin do django

class Usuario(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.EmailField()
    senha = models.CharField(max_length = 64)

    def __str__(self) -> str:
        return self.nome
        
