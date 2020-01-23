from django.test import TestCase

from .models import Product

class ProductTestClass(TestCase):
    # setup method
    def setUp(self):
        self.product1 = Product(p_name = 'someproduct',
        p_image = 'image.jpg' ,
        size = '120g' ,
        qyt = 22,
        price = 20.20,
        category = 'mild',
        date = '12-12-2020')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.product1,Product))

        # saving method
    def test_save_method(self):
        self.product1.save_product()
        product1 = Product.objects.all()
        self.assertTrue(len(product1) > 0)

      #tear down method
    def tearDown(self):
        Product.objects.all().delete()

        # delete method
    def test_delete_method(self):
        self.product1.save_product()
        self.product1.delete_product()
        product1 = Product.objects.all()
        self.assertTrue(len(product1)== 0 )