from django.db import models
from client.models import Client
from products.models import Product
import datetime as dt

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save_sale(self):
        self.save()

    def delete_sale(self):
        self.delete()

    def get_total(self):
        result = self.product.product_price * self.quantity
        return result

    @classmethod
    def todays_sales(cls):
        today = dt.date.today()
        sale = cls.objects.filter(date__date = today)
        return sale

    def __str__(self):
        return f'{self.client}'

    class Meta:
        ordering = ['-date']

