from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'pokemons'