from django import forms

from .models import Product


class ProductSearchForm(forms.Form):
    search_title = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Поиск по названию...'}))



class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


    price = forms.DecimalField(max_digits=7,decimal_places=2,min_value=0,)
    remainder = forms.IntegerField(min_value=0,)


    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'price', 'image', 'remainder')
