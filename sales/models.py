from django.db import models
from client.models import Client
from products.models import Product
class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def save_sale(self):
        self.save()

    def delete_sale(self):
        self.delete()

    def __str__(self):
        return f'{self.client_name}'

    class Meta:
        ordering = ['-date']

