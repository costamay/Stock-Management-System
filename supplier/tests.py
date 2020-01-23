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