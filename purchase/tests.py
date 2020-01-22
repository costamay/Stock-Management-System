from django.test import TestCase
from .models import Purchase

class PurchaseTestClass(TestCase):
    # setup method
    def setUp(self):
        self.purchase1 = Purchase(pu_date = '01-01-2020', qyt = 200.01 , price = 90.12 )

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.purchase1,Purchase))

    # saving instance

    # def test_save_method(self):
    #     self.purchase1.save_purchase()
    #     purchase1 = Purchase.objects.all()
    #     self.assertTrue(len(purchase1) > 0)