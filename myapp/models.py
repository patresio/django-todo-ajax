from django.db import models

# Create your models here.
## ⛔️ a Fazer, ⚠️ Fazendo e ✅ Finalizado
class Status(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class TodoList(models.Model):
    titulo = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', to_field='id', default='1')

    def __str__(self):
        return self.nome