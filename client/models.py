from django.db import models
from products.models import *

class Client(models.Model):
    c_name = models.CharField(max_length=100)
    c_phone = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save_client(self):
        self.save()

    def delete_client(self):
        self.delete()

    @classmethod   
    def update_supplier(cls,id,new_name):
        cls.objects.filter(pk = id).update(c_name=new_name)
        new_name_object = cls.objects.get(c_name = new_name)
        new_name = new_name_object.name
        return new_name

    def __str__(self):
        return f'{self.c_name}'

    class Meta:
        ordering = ['-date']