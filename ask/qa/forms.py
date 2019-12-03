from django import forms
# from django.forms import ModelForm

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
		self.cleaned_data ['author_id'] = '1'
#		quest = Question(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
		quest = Question(**self.cleaned_data)
		quest.save()
		return quest



"""
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
"""


class AnswerForm(forms.Form):
	"""docstring for AnswerForm"""

	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget = forms.HiddenInput)

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text

	def clean_question(self) :
		try :
			quest_id = int(self.cleaned_data['question'])
		except ValueError :
			raise forms.ValidationError('fail input')
		return quest_id

	def save(self) :
		answer = Answer(text=self.text, question=self.question)
		answer.save()
		return answer
