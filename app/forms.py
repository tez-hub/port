from email import message
from socket import fromshare
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'subject'}))
    recipient = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'message'}))