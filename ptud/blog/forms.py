from django import forms
from .models import Task, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    finished = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # Sử dụng HTML5 datetime-local
            'class': 'form-control'
        }),
        required=True  # Bắt buộc nhập
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'finished']


