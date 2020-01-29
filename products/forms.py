from django import forms
from products.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name' ,'product_size','product_qyt','product_price','product_category')
    
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        self.fields['product_category'].empty_label = "Select"

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


        
