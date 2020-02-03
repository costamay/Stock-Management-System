from django.db import models
from products.models import Product
from django.db.models import Q

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone = models.IntegerField()
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

    @classmethod
    def search(cls,searchterm):
        search = cls.objects.filter(Q(client_name__icontains=searchterm))
        return search

    def __str__(self):
        return f'{self.client_name}'

    class Meta:
      ordering = ['-date']
