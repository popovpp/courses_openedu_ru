from django import forms


class StartForm(forms.Form):
	searchWords = forms.CharField(label='Введите слово или фразу в названии курса', max_length=255, error_messages={'required': ''})
	
