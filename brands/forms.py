from django import forms
from . import models


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ["name", "description"]  # campos do bd que serão consumidos
        widgets = {  # transformando a aparência do formulário via forms e não no html
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "name": "Nome",
            "description": "Descrição",
        }
