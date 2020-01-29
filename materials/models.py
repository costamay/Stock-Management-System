from django.db import models
from django.db.models import Q


class Material(models.Model):
    material_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def save_material(self):
        self.save()

    def delete_material(self):
        self.delete()

    @classmethod   
    def update_supplier(cls,id,new_name):
        cls.objects.filter(pk = id).update(m_name=new_name)
        new_name_object = cls.objects.get(m_name = new_name)
        new_name = new_name_object.name
        return new_name

    @classmethod
    def search(cls,searchterm):
        search = cls.objects.filter(Q(material_name__icontains=searchterm))
        return search

    def __str__(self):
        return f'{self.material_name}'

    class Meta:
        ordering = ['date']
