from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'category', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()  # нужно вызывать
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Контент',
            'rate': 'Рейтинг',
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
