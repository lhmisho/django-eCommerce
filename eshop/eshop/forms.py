from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname    = forms.CharField(label='Full name', max_length=120, widget=forms.TextInput(attrs={"class" : "form-control", "id": "fullname", "placeholder":"Full name"}))
    email       = forms.EmailField(label='Email', max_length=120, widget=forms.EmailInput(attrs={"class" : "form-control", "id" : "contactId", "placeholder" : "Email"}))
    content     = forms.CharField(label='Description', max_length=500, widget=forms.Textarea(attrs={"class" : "form-control", "id" : "contactDescription", "placeholder" : "Write something about your topic"}))

    # a simple example of email validation
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'gmail.com' not in email:
            raise forms.ValidationError("Email has to be GMAIL")
        return email

# creating class for login form ... next step is manage views.py       
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    # check weather the user is already exist ro not 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError("Username already exists!")
        else:
            return username

    # check weather the email is already exits or not
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError("Email is already exists!")
        else:
            return email

    # check weather the password are matched or not
    def clean(self):
        data = self.cleaned_data
        password = self.data.get('password')
        password2 = self.data.get('password2')

        if password != password2:
            raise forms.ValidationError("Password must be the same!")
        else:
            return data