from django import forms

class NameForm(forms.Form):
    title_text = models.CharField(max_length=140)
    body_text = forms.TextField(label='Body Text')