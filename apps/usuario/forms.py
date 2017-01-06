from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
	
	class Meta:
		model = User

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username': 'NOMBRE DE USUARIO',
			'first_name':'NOMBRE',
			'last_name':'APELLIDOS',
			'email':'CORREO',	
		}

