from django import forms
from .models import *

Genre_Choices= [
    ('Landscape', 'Landscape'),
    ('Portrait', 'Portrait'),
    ('Street', 'Street'),
    ('Long Exposure', 'Long Exposure'),
    ]
  
class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        fields = ['Name', 'Mail', 'Phone', 'Description']
        labels = {
            "Name": "Name",
            "Mail": "E-Mail",
            "Phone": "Contact Number",
            "Description": "Description",
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Mail': forms.TextInput(attrs={'class':'form-control'}),
            'Phone': forms.TextInput(attrs={'class':'form-control'}),
            'Description': forms.TextInput(attrs={'class':'form-control'})
        }