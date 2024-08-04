import re

from django import forms

from product.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"

    def clean_contry(self):
        country = self.cleaned_data.get("contry")
        if not re.match(r"^[a-zA-Z\s]+$", str(country)):
            raise forms.ValidationError("Country field can only contain letters.")
        return country

    def clean_color(self):
        color = self.cleaned_data.get("color")
        if not re.match(r"^[a-zA-Z\s]+$", str(color)):
            raise forms.ValidationError("Model field can only contain letters.")
        return color


class PhoneUpdateForm(forms.ModelForm):
    model = forms.CharField(max_length=14, disabled=True)

    class Meta:
        model = Phone
        fields = ["model", "price", "status", "inventory", "color"]
