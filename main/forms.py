from django import forms
import datetime
from .models import *

now = datetime.datetime.now()


class AddCourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрана'

    class Meta:
        model = Courses
        fields = ['title', 'description', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class SearchCourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрана'

    class Meta:
        model = Courses
        fields = ['title', 'description', 'category', 'author']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
