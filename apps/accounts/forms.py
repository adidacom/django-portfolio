from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("User is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', help_text="Required. Please provide valid email.")
    # email2 = forms.EmailField(label='Email confirmation', help_text="Enter the same email as before, for verification.")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            # 'email2',
            'password1',
            'password2',
        ]

    # def clean_email2(self):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("Email already registered")
    #     return email

