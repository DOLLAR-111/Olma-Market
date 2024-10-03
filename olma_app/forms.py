from django import forms
from .models import CardInfo

class CardInfoForm(forms.ModelForm):
    class Meta:
        model = CardInfo
        fields = ['card_number', 'expiry_date', 'full_name']
        widgets = {
            'card_number': forms.TextInput(attrs={'placeholder': '0000 0000 0000 0000', 'maxlength': '16'}),
            'expiry_date': forms.TextInput(attrs={'placeholder': 'MMYY', 'maxlength': '4'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Ism Familiya'}),
        }
