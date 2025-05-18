from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=256)
    content = forms.CharField(max_length=556)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
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
