from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    title = forms.CharField()
    reward = forms.IntegerField()

    class Meta:
        model = Question
        fields = '__all__'