from django.test import TestCase

from .models import Supplier
from materials.models import Material

class SupplierTestClass(TestCase):
    # setup method
    def setUp(self):
        self.supplier1 = Supplier(s_name = 'farmer',
        s_phone = '0712345678' ,
        date = '20-12-2020' ,
        materials = Material.objects.create(m_name = 'onion', qyt = 2.0 , price = 200.0 , date = '01-01-2020'))

      # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.supplier1,Supplier))

       # saving method
    def test_save_method(self):
        self.supplier1.save_supplier()
        supplier1 = Supplier.objects.all()
        self.assertTrue(len(supplier1) > 0)

      #tear down method
    def tearDown(self):
        Supplier.objects.all().delete()

    # delete method
    def test_delete_method(self):
        self.supplier1.save_supplier()
        self.supplier1.delete_supplier()
        supplier1 = Supplier.objects.all()
        self.assertTrue(len(supplier1)== 0 )