from simpleprojectmanagement.models import Supervisor, Developer
from django import forms
# This line imports the Django forms package
class NewDeveloper(forms.Form):
     name = forms.CharField(label="Name", max_length=30)
     login = forms.CharField(label="Login", max_length=30)
     password = forms.CharField(label="Password", widget=forms.PasswordInput)
     supervisor = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())
