from django.db import models
from orders.models import Order

# Create your models here.
class Ticket(models.Model):
    number = models.CharField('Número', max_length=100, unique=True)
    problem = models.CharField('Problema', max_length=100)
    issue_date = models.DateField('Data de emissão', auto_now_add=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='ticket')

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticket'
        ordering = ['id']

    def __str__(self):
        return f'{self.number}'
