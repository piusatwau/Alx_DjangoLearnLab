from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField(label='Your full name', max_length=50)
    email = forms.EmailField(label='Your email ID')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    
