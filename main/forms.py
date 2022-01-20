from django import forms
import datetime
from .models import *

now = datetime.datetime.now()


class AddCourseForm(forms.ModelForm):
    tags = forms.CharField(max_length=500,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите теги (через запятую)'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория'

    class Meta:
        model = Courses

        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название курса'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'Описание курса'}),
        }

class EditCourseForm(forms.ModelForm):
    tags = forms.CharField(max_length=500,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите теги (через запятую)'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория'

    class Meta:
        model = Courses

        fields = ['title', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название курса'}, ),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'Описание курса'}),
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
