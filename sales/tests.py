from django.test import TestCase

from .models import Sale
from client.models import Client
from products.models import Product

class SaleTestClass(TestCase):
    # setup method
    def setUp(self):
        self.sale1 = Sale(client = Client.objects.create(c_name = 'Naivas', c_phone = 11 , date = '10-10-2020', 
        product = Product.objects.create(p_name = 'someproduct',
        p_image = 'image.jpg' ,
        size = '120g' ,
        qyt = 22,
        price = 20.20,
        category = 'mild',
        date = '12-12-2020')),
        date = '12-12-2020'
        ),

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sale1,Sale))
   