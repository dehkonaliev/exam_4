from django import forms
from .models import Category, Product

class NewProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    desc = forms.CharField(max_length=1000, widget=forms.Textarea)
    price = forms.DecimalField()
    is_available = forms.BooleanField(initial=True, required=False)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'desc', 'price', 'is_available', 'image']