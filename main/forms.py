from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрана'
        self.fields['author'].empty_label = 'Не выбрана'
    class Meta:
        model = Courses
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
