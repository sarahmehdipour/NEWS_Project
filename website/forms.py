


from django import forms


# class ContactForm(forms.Form):
#   name=forms.CharField(max_length=60)
#   email=forms.EmailField(max_length=254)
#   subject=forms.CharField(max_length=254)
#   message=forms.CharField(widget=forms.Textarea)


from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model=Contact
    fields='__all__'
    