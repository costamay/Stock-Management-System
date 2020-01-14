from django.db import models
from client.models import Client
from products.models import Product

DELIVERY_TYPE_CHOICES = (
    (1, 'delivered'),
    (2,'in progress'),
    (3,'cancelled')
)
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qyt =models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    order_no = models.CharField(max_length=100)
    delivery_status = models.PositiveSmallIntegerField(choices = DELIVERY_TYPE_CHOICES)

    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()
    
    def update_order(self):
        self.update()

    def __str__(self):
        return f'{self.order_no}'

    class Meta:
        ordering = ['-date']