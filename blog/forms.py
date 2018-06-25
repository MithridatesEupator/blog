from django import forms
from .models import Post

class make_post_form(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols':'70','rows':'1'}), label='')
    post_text = forms.CharField(widget=forms.Textarea, label='')
    #class Meta:
        
    #post_image = forms.ImageField()
    #published_date = forms.DateTimeField()
    
class delete_post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = []