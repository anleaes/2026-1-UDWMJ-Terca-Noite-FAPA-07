from django.db import models
from persons.models import Person
from socialnetworks.models import Socialnetwork

# Create your models here.
class Player(Person):
    gender = models.CharField('Genero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    nickname = models.CharField('Apelido', max_length=20),
    socialnetwork = models.ManyToManyField(Socialnetwork, verbose_name="Redes Socias")

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =['id']

    def __str__(self):
        return super().first_name
        # ou pode ser usado "return super().__str__()"
