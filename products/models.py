from django.db import models

CATEGORY = (
    ('N','without chillie'),
    ('H',' hot chillie'),
    ('M','mild chillie'),
    ('SP','siri ya pilau'),
    ('SM','siri ya mchuzi'),
    ('SC','siri ya chai')
)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='images/')
    product_size = models.CharField(max_length=50)
    product_qyt = models.PositiveIntegerField()
    product_price = models.FloatField()
    product_category = models.CharField(max_length=50,choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)

    def save_product(self):
        self.save()

  
    @classmethod
    def update_supplier(cls, id, new_name):
        cls.objects.filter(pk=id).update(p_name=new_name)
        new_name_object = cls.objects.get(p_name=new_name)

        new_name = new_name_object.name
        return new_name

    def __str__(self):
        return f'{self.product_name}'

    class Meta:

        ordering = ['-date']

