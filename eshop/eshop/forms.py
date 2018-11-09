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
