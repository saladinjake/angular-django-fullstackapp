from simpleprojectmanagement.models import Supervisor, Developer
from django import forms
# This line imports the Django forms package

class NewUser(forms.form):
    username = forms.CharField(max_length=50, label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20, label="Phone number" )
    age = forms.DateField(label="age" )
    last_login = forms.DateTimeField(label="Date of last connection")
    email = forms.EmailField(label="Email")
    experience_role = forms.IntegerField(label="Senior",initial=0)
    date_created = forms.DateField(label="Date of Birthday",auto_now_add=True)

class NewDeveloper(forms.Form):
    supervisedby = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())

class NewSupervisor(NewUser):
    specialisation = models.CharField(max_length=50, label="Specialisation")
