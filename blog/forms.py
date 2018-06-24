from django import forms

class make_post_form(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'cols':'70',
'rows':'1'}), label='')
    post_text = forms.CharField(widget=forms.Textarea, label='')
    #class Meta:
        
    #post_image = forms.ImageField()
    #published_date = forms.DateTimeField()