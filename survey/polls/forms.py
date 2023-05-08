from django import forms
from .models import Survey

class StoreNameForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['name']
        labels = {
            'name': 'What is the name of your store?'}

class BalanceForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['balance']
        widgets = {
            'balance': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
        }
        labels = {
            'balance': 'What is the balance left on your gift card?'
        }

class PriceForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['price']
        widgets = {
            'price': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
        }
        labels = {
            'price': 'What price are you selling at?'
        }

class NetworkForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['network']
        labels = {
            'network': 'Which network would you like to receive funds at?'
        }
class AddressForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['address']
        labels = {
            'address': 'What address do you want to receive funds at?'
        }
class EmailForm(forms.ModelForm):
       class Meta:
        model = Survey
        fields = ['email']
        labels = {
            'email': 'What’s your email address?'
        }