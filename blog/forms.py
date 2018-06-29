from django import forms
from .models import *

class make_post_form(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols':'70','rows':'1'}), label='')
    post_text = forms.CharField(widget=forms.Textarea, label='')
    post_image = forms.ImageField(label='', required=False)
    
class make_comment_form(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea, label='')
    
class delete_post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = []
        
class delete_comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = []