from django.db import models
from materials.models import *
import datetime as dt



class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_contact = models.CharField(max_length=14)
    date = models.DateTimeField(auto_now_add=True)
    materials = models.ForeignKey(Material, on_delete=models.CASCADE)

    def save_supplier(self):
        self.save()

    def delete_supplier(self):
        self.delete()



    @classmethod
    def update_supplier(cls, id, new_name):
        cls.objects.filter(pk=id).update(s_name=new_name)
        new_name_object = cls.objects.get(s_name=new_name)

        new_name = new_name_object.name
        return new_name

    @classmethod
    def todays_purchase(cls):
        today = dt.date.today()
        purchase = cls.objects.filter(date__date = today)
        return purchase


    def __str__(self):
        return f'{self.supplier_name}'

    class Meta:
        ordering = ['-date']
