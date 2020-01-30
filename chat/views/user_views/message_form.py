from django import forms

class Message_form(forms.Form):
    text = forms.CharField(label = "",max_length=1000)