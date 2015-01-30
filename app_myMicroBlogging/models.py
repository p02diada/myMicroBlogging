from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your models here.

class my_user(User):
	seguidos=models.ManyToManyField("self", symmetrical =False, blank =True, null=True)
	

class micro_post(models.Model):
	contenido = models.CharField(max_length=150)
	usuario = models.ForeignKey(my_user)
	fecha = models.DateTimeField(auto_now=True)

class favorito(models.Model):
	micro_post = models.ForeignKey(micro_post)
	usuarios = models.ForeignKey(my_user, null=True, blank=True)

class lista(models.Model):
	nombre=models.CharField(max_length=30, unique=True)
	usuario=models.ForeignKey(my_user, related_name='identificador')
	listaUsuarios=models.ManyToManyField(my_user)

class hashtag(models.Model):
	nombre=models.CharField(max_length=140, unique=True)
	repeticiones=models.IntegerField(default=0)
	micro_post = models.ManyToManyField(micro_post,symmetrical=True)



