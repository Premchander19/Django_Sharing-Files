from django import forms
from .models import Data
from django.forms import ClearableFileInput


# class Send(forms.ModelForm):
#     class Meta:
#         model = Data
#         fields = ('file', 'text')
#         widgets = {
#             'file': ClearableFileInput(attrs={'multiple': True}),
#         }
class Send(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
