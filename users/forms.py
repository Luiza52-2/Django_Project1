from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=8)
    email = forms.EmailField(required=False) 
    age = forms.IntegerField(required=False)
    image = forms.ImageField(required=False)
    password = forms.CharField()
    password_confirm = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get ('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError('passwords should match')
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)   