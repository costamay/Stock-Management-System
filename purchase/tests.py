from django.test import TestCase
from django.utils import timezone
from .models import Purchase
from materials.models import Material
from supplier.models import Supplier

class PurchaseTestClass(TestCase):
    # setup method
    def setUp(self):
        self.purchase1 = Purchase(pu_date = '01-01-2020',
        qyt = 200.01 ,
        price = 90.12 ,
        material = Material.objects.create(m_name = 'onion', qyt = 2.0 , price = 200.0 , date = '01-01-2020'),
        supplier = Supplier.objects.create(s_name = 'farmer' , s_phone = '0712345678', date = '10-10-2020' ,
        materials = Material.objects.create(m_name = 'onion', qyt = 2.0 , price = 200.0 , date = '01-01-2020')))

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.purchase1,Purchase))

    # saving method
    def test_save_method(self):
        self.purchase1.save_purchase()
        purchase1 = Purchase.objects.all()
        self.assertTrue(len(purchase1) > 0)
    #tear down method
    def tearDown(self):
        Purchase.objects.all().delete()
    # deleting method
    def test_delete_method(self):
        self.purchase1.save_purchase()
        self.purchase1.delete_purchase()
        purchase1 = Purchase.objects.all()
        self.assertTrue(len(purchase1)== 0 )