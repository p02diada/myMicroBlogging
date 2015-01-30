from django.forms import ModelForm
from django import forms
from app_myMicroBlogging.models import my_user, micro_post, lista
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import AuthenticationForm


class my_user_form(ModelForm):
	class Meta:
		model=my_user
		fields = ['username', 'password', 'email']

class my_micro_post(ModelForm):
	class Meta:
		model=micro_post
		fields = ['contenido']
class edit_my_user_form(ModelForm):
	class Meta:
		model=my_user
		fields=['username', 'first_name', 'last_name', 'email']

class lista_form(ModelForm):
	class Meta:
		model=lista
		fields=['nombre']
