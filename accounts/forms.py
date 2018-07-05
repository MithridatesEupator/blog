from django.contrib.auth import get_user_model
from django import forms
from .models import *
from django.db.models import Q

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password do not match")
        return password2
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False) 
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user
    
class UserLoginForm(forms.Form):
    query = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get("query")
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
                Q(username__iexact=query) | 
                Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("User does not exist, Bitch")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Invalid Login")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)
    
    
class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = []
        
class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_pic']
        
    def __init__(self, *args, **kwargs):
        super(EditUser, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['bio'].required = False
        self.fields['profile_pic'].required = False