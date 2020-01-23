from django.test import TestCase

from .models import Product

class ProductTestClass(TestCase):
    # setup method
    def setUp(self):
        self.product1 = Product(p_name = 'someproduct',
        p_imge = 'image.jpg' ,
        size = '120g' ,
        qyt = 22,
        price = 20.20,
        category = 'mild',
        date = '12-12-2020')