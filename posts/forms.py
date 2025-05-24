from django import forms
from .models import Category, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'category', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Контент',
            'category': 'Категория',
            'tags': 'Теги'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and title.lower() == 'python':
            raise forms.ValidationError('Title cannot be "Python"')
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title.lower() == content.lower():
            raise forms.ValidationError('Title and Content cannot be the same')

        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=256, required=False)
    category_id = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False)
    
    orderings = (
        ('created_at', 'Creation date'),
        ('-created_at', 'Creation date (desc)'),
        ('rate', 'Rate'),
        ('-rate', 'Rate (desc)'),
        (None, 'No ordering')
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)