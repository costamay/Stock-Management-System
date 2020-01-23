from django.test import TestCase
from .models import Material

class MaterialTestClass(TestCase):
    # setup method
    def setUp(self):
        self.material1 = Material(m_name = 'onion',
        qyt = 10.00 ,
        price = 100.98 ,
        date = '01-12-2020' )

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.material1,Material))

        # saving method
    def test_save_method(self):
        self.material1.save_material()
        material1 = Material.objects.all()
        self.assertTrue(len(material1) > 0)

        #tear down method
    def tearDown(self):
        Material.objects.all().delete()

        # delete method
    def test_delete_method(self):
        self.material1.save_material()
        self.material1.delete_material()
        material1 = Material.objects.all()
        self.assertTrue(len(material1)== 0 )