from django.db import models

# Create your models here.

class Dog(models.Model):

    RESCATADO = 'Rescatado'
    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'

    STATE_CHOICES = (
        (RESCATADO, 'Rescatado'),
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
    )

    photo = models.ImageField(upload_to='dog_image', blank=True)
    name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RESCATADO)

class User(models.Model):

    YES = '1'
    NO = '0'

    STATE_CHOICES = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    admin = models.CharField(max_length=10, choices=STATE_CHOICES, default=NO)
