from django import forms

from product.models.product import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"
