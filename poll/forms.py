from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_text', 'option1', 'option2', 'option3']
