from django import forms 
from django.contrib.auth.models import User
from .models import *

class contacto_form(forms.Form):
	correo 	= forms.EmailField(widget=forms.TextInput())
	titulo	= forms.CharField(widget=forms.TextInput())
	texto	= forms.CharField(widget=forms.Textarea())


class agregar_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class login_form (forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave   = forms.CharField(widget=forms.PasswordInput(render_value=False))


class register_form (forms.Form):
	username 		= forms.CharField(widget=forms.TextInput())
	email 			= forms.EmailField(widget=forms.TextInput())
	password_1 		= forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
	password_2   	= forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo Electronico ya Existe')

	def clean_password_2(self):#hace la validacion del password_2
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']
		
		if password_1==password_2:
			pass
		else:
			raise forms.ValidationError('PAsswords no Coinciden')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'