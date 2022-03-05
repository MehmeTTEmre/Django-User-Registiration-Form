from django import forms
from .models import Form

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'