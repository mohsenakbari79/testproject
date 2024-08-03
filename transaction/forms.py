from django import forms

from transaction.models import Transaction




class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["product", "inventory", "entrance"]

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get("product")
        inventory = cleaned_data.get("inventory")
        entrance = cleaned_data.get("entrance")

        if not entrance and inventory > product.inventory:
            raise forms.ValidationError(
                "The transaction inventory cannot exceed the product inventory."
            )
        return cleaned_data
