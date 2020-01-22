from django.test import TestCase
from .models import Supplier

class SupplierTestClass(TestCase):
    # setup method
    def setUp(self):
        self.supplier1 = Supplier(s_name = 'Farmer', s_phone = '0712345678' , date = '01-01-2020' )

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.supplier1,Supplier))

