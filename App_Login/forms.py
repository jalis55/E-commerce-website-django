from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from App_Login.models import User,Profile

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)

class UserForm(UserCreationForm):
    
    model=User
    class Meta:
        fields=('email','password1','password2',)
