from django import forms
from myapp.models import User

class UserForm(forms.ModelForm):  
    user_email = forms.CharField(max_length=70,widget=forms.TextInput(attrs={'placeholder':'Enter Email '}))
    user_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder':'Enter Username '}))
    user_password = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder':'Enter Password'}))
    
    class Meta:
        model = User
        fields = ["user_email","user_name","user_password"]
        labels = {
            "user_email": "",
            "user_name": "",
            "user_password": ""
        }


