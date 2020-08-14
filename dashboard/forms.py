from django import forms
from .models import ContactMessage

class AddNotificationForm(forms.Form):
    title=forms.CharField(max_length=50, required=False)
    body=forms.CharField( max_length=200, required=True)
    icon=forms.CharField( max_length=200, required=True)
    color=forms.CharField( max_length=200, required=True)
    link=forms.CharField( max_length=1100, required=False)
    priority=forms.IntegerField(required=False)
    profile_id=forms.IntegerField(required=True)

class SearchForm(forms.Form):
    search_for=forms.CharField(max_length=20, required=True)

class AddLinkFrom(forms.Form):
    title=forms.CharField(max_length=200, required=True)
    url=forms.CharField(max_length=1100, required=True)
    row_number=forms.IntegerField(required=True)
class UploadProfileImageForm(forms.Form):
    profile_id=forms.IntegerField(required=True)
    image=forms.ImageField(required=True)

  
class ContactMessageForm(forms.ModelForm):
    
    class Meta:
        model = ContactMessage
        fields = ("fname","lname","email","subject","message")

class EditProfileForm(forms.Form):

    profile_id=forms.IntegerField(required=True)
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)
    mobile=forms.CharField(max_length=50, required=False)
    region_id=forms.CharField(max_length=50, required=False)
    address=forms.CharField(max_length=50, required=False)
    bio=forms.CharField(max_length=500, required=False)

class ChangeProfileForm(forms.Form):
    actived=forms.IntegerField(required=True)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50, required=True)
    password=forms.CharField(max_length=150, required=True)

class ResetPasswordForm(forms.Form):
    username=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control leo-farsi mt-3','placeholder':'موبایل','type':'tel'}))
    old_password=forms.CharField(max_length=150, required=False)
    new_password=forms.CharField(max_length=150, required=True)
class RegisterForm(forms.Form):
    region_id=forms.IntegerField(required=True)
    username=forms.CharField(max_length=50, required=True)
    password=forms.CharField(max_length=150, required=True)
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)