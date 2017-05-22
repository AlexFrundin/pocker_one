#import django.forms as df
from django import forms
from django.core.exceptions import ValidationError

def name_validator(name):
    if not name.startswith('Mr.'):
        raise ValidationError('Only for men')
    return name

class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Отзыв', widget=forms.Textarea())
    nick = forms.CharField(label='Имя', validators =(name_validator,))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_feedback(self):#пеегрузка функции валидации для класса feedback
        if "windows" in self.cleaned_data['feedback'].lower():
            raise ValidationError('Windows is in form')
        return self.cleaned_data['feedback']
