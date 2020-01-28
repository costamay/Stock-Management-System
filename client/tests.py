from django.test import TestCase

from .models import Client
from products.models import Product

class ClientTestingClass(TestCase):
     # setup method
    def setUp(self):
        self.client1 = Client(c_name = 'Naivas',
        c_phone = '0712345678' ,
        date = '20-12-2020' ,
        product = Product.objects.create(p_name = 'pilau', p_image = 'image.jpg' , size = '100.60' , qyt = 12, price = 20.23 , category = '1', date = '20-12-2020'))