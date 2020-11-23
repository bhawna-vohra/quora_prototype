from django import forms
from quora.models import UserProfileInfo   
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	pic = forms.ImageField(required=False)	
	class Meta():
		model = UserProfileInfo
		fields = ('pic',)
		exclude = ('user',)

class UserFormLogin(forms.Form):
	
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput)
	
	fields = ('username','password')

