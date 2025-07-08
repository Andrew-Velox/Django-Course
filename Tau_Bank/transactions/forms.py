from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields =['amount','transaction_type']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposite_amount = 100
        amount = self.cleaned_data.get('amount')

        if amount < min_deposite_amount:
            raise forms.ValidationError(
                f"You Need to deposite at least {min_deposite_amount} $"
            )
        return amount
    

class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account  = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        # print(balance)
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f"You Need to withdraw at least {min_withdraw_amount} $"
            )
        elif amount > max_withdraw_amount:
            raise forms.ValidationError(
                f"You Need to withdraw at most {max_withdraw_amount} $"
            )
        elif amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your Account.'
                'You Can not withdraw more then your Account Balance.'
            )
        return amount
    

class LoanRequestForm(TransactionForm):

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        
        return amount
    
    


