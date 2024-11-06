from django import forms
from .models import Adoption


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'id': 'id_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'id': 'id_email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'id': 'id_message', 'rows': 5}))


class AboutForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    phone = forms.CharField(max_length=15, label="Phone Number")  
    request = forms.CharField(widget=forms.Textarea, label="Your Request")
    
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'
        widgets = {
            'current_pets': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Species, Breed, Name, Age, Sex, Altered (yes/no)'}),
            'residents': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Names and ages of all permanent residents of your home'}),
            'vet_reference': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Vet name, address & phone number'}),
            'comments': forms.Textarea(attrs={'rows': 4}),
            'additional_reference': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Your pet sitter, doggie daycare contact, etc.'}),
        }
