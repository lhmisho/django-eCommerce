from django import forms

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