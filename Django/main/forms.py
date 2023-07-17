from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Test,Question,Answer


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1","password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	


class NewTestForm(forms.ModelForm):
	title = forms.CharField(label="Название", max_length=100)
	class Meta:
		model = Test
		fields = ['title']


class NewQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['text']


class NewAnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['text','is_correct']
