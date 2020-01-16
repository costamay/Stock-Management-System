from django.db import models
from supplier.models import *
from materials.models import Material



class Purchase(models.Model):
    pu_date = models.DateTimeField(auto_now_add=True)
    qyt = models.FloatField()
    price = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def save_purchase(self):
        self.save()

    def delete_purchase(self):
        self.delete()

    def __str__(self):
        return f'{self.material}'

    class Meta:

        ordering = ['-pu_date']

