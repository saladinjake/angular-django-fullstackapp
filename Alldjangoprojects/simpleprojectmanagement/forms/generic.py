from simpleprojectmanagement.models import Supervisor, Developer
from django import forms
import datetime

# This line makes use of the Django forms.Form package

YEARS= [x for x in range(1940,2021)]
class NewUserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField( widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20, label="Phone number", widget=forms.TextInput(attrs={'placeholder':'phone'}) )
    age = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS) )
    last_login = forms.DateTimeField(initial=datetime.date.today, label="Last Login", widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder':'email'}))
    experience_role = forms.IntegerField(label="Senior",initial=0, widget=forms.TextInput(attrs={'placeholder':'Seniority'}))
    date_created = forms.DateTimeField(initial=datetime.date.today, label="Created Date")


class NewDeveloperForm(NewUserForm):
    supervisedby = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())

class NewSupervisorForm(NewUserForm):
    specialisation = forms.CharField(max_length=50, label="Specialisation")




class EditUserForm(forms.Form):


    username = forms.CharField(max_length=50, label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20, label="Phone number" )
    age = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS) )
    last_login = forms.DateTimeField(initial=datetime.date.today, label="Last Login", widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label="Email")
    experience_role = forms.IntegerField(label="Senior",initial=0)
    date_created = forms.DateTimeField(initial=datetime.date.today, label="Created Date")
class EditDeveloperForm(EditUserForm):
    supervisedby = forms.ModelChoiceField(label="Supervisor",queryset=Supervisor.objects.all())

class EditSupervisorForm(EditUserForm):
    specialisation = forms.CharField(max_length=50, label="Specialisation")


# This lines makes use of the Django forms.ModelForm package
