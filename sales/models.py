from django.db import models
from client.models import Client
from products.models import Product
from django.utils import timezone
import datetime as date

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)

    def save_sale(self):
        self.save()

    def delete_sale(self):
        self.delete()

    def get_total(self):
        result = self.product.product_price * self.quantity
        return result

    # def final_quantity(self):
        
    #     # import pdb; pdb.set_trace()
    #     return obj.product_qyt

    @classmethod
    def todays_sales(cls):
        today = dt.date.today()
        sale = cls.objects.filter(date__date = today)
        return sale

    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(user__name__icontains = name)

    def __str__(self):
        return f'{self.client}'

    class Meta:
        ordering = ['-date']

