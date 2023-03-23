from django import forms

class UserQueryForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
