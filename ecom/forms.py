from django import forms
from .models import Transaction 
from django.forms import ModelForm, Textarea
class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['firstname', 'lastname', 'address', 'phone', 'message']
        widgets = {
            'firstname': Textarea(attrs={'cols': 70, 'rows': 1}),
            'lastname': Textarea(attrs={'cols': 70, 'rows': 1}),
            'address': Textarea(attrs={'cols': 70, 'rows': 1}),
            'phone': Textarea(attrs={'cols': 70, 'rows': 1}),
            'message': Textarea(attrs={'cols': 70, 'rows': 1}),
        }