from django.db import models
from players.models import Player
from supports.models import Support

# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField('Forma de pagamento', max_length=20, null=True, blank=True, default='Dinheiro',choices=[
        ('Dinheiro', 'Dinheiro'),
        ('Pix', 'Pix'),
        ('Cartao de Credito', 'Cartao de Credito'),
        ('Cartao de Debito', 'Cartao de Debito'),
    ])
    status = models.CharField('Status', max_length=20, null=True, blank=True, default='Em andamento',choices=[
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    ])
    total = models.FloatField('Preco Total', null=True, blank=True, default=0.0)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return f'{self.id}' 
