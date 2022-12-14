from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# Create your forms here.

class UserCreateForm(UserCreationForm):
	"""
	Formed used for user creation.
	"""

	email = forms.EmailField(required=True)

	class Meta:
		model = get_user_model()
		fields = ("username", "password1")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields =  ("first_name","last_name","phone_number", "email","home_address","location")