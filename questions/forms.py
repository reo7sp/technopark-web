from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32)


class SignupForm(forms.Form):
    login = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=32)
    nickname = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=32, widget=forms.PasswordInput())
    avatar = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('password_confirmation'):
            self.add_error('password_confirmation', 'Password and password confirmation must match')
