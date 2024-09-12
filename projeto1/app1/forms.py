from django import forms
from .models import User

#modelform
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

#form.form