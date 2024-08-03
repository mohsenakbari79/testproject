from django import forms

from product.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"


class PhoneUpdateForm(forms.ModelForm):
    model = forms.CharField(max_length=14, disabled=True)

    class Meta:
        model = Phone
        fields = ["model", "price", "status", "inventory", "color"]


