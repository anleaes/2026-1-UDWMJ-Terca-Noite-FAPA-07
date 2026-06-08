from django.db import models
from description.models import Description

# Create your models here.
class Game(models.Model):
    name = models.CharField('Nome', max_length=50)
    brand = models.TextField('Marca', max_length=50)
    launch_date = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False) 
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'
