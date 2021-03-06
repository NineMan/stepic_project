from django import forms
# from django.forms import ModelForm

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Question, Answer
from datetime import datetime


"""
class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
"""


class AskForm(forms.Form):
	"""docstring for AskForm"""

	title = forms.CharField(max_length = 100)
	text = forms.CharField(widget = forms.Textarea)

	def clean_title(self):
		title = self.cleaned_data['title']
		if title.strip() == '':
			raise forms.ValidationError('Title could not be empty', 
                                        code='validation_error')
		return title


	def clean_text(self):
		text = self.cleaned_data['text']
		if text.strip() == '':
			raise forms.ValidationError('Text could not be empty',
                                        code='validation_error')
		return text


	def save(self):

#		if self._user.is_anonymous():
#			self.cleaned_data['author_id'] = 1
#		else:
#			self.cleaned_data['author_id'] = self._user

#		self.cleaned_data ['author_id'] = '1'
		self.cleaned_data ['author_id'] = self._user.id
#		question = Question(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
		question = Question(**self.cleaned_data)
		question.save()
		return question



"""
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
"""


class AnswerForm(forms.Form):
	"""docstring for AnswerForm"""

	text = forms.CharField(widget=forms.Textarea(attrs={'rows':'2'}), help_text='My answer')
#	question = forms.IntegerField(widget = forms.HiddenInput)
#	question = forms.IntegerField()
	question = forms.ModelChoiceField(queryset=Question.objects.all())

#	def clean_text(self) :
#		text = self.cleaned_data['text']
#		return text
#
#	def clean_question(self) :
#		try :
#			quest_id = int(self.cleaned_data['question'])
#		except ValueError :
#			raise forms.ValidationError('fail input')
#		return quest_id

	def save(self) :
#		self.cleaned_data['author'] = self._user
#		answer = Answer(text=self.cleaned_data['text'], question=self.cleaned_data['question'], )
#		answer.save()
#		return answer

		answer = Answer(**self.cleaned_data)
#		answer.author_id = self._user.id
		answer.author_id = '1' # self._user.id
		answer.save()
		return answer


class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.EmailField()

	def clean_username(self):
		return self.cleaned_data['username']

	def clean_password(self):
		return self.cleaned_data['password']

	def clean_email(self):
		return self.cleaned_data['email']

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['password'])
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password'])
		user.save()
		return user


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def clean_username(self):
		return self.cleaned_data['username']

	def clean_password(self):
		return self.cleaned_data['password']

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
		if user:
			return user
		else:
			raise forms.ValidationError('invalid username/password')
