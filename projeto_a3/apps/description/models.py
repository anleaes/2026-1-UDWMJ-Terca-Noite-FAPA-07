from django.db import models

# Create your models here.
class Description(models.Model):
    category = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Descricao'
        verbose_name_plural = 'Descricoes'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.name}'
