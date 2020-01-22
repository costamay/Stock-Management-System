from django.test import TestCase
from .models import Material

class MaterialTestClass(TestCase):
    # setup method
    def setUp(self):
        self.material1 = Material(m_name = 'onion', qyt = 10.00 , price = 100.98 ,date = '01-12-2020' )

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.material1,Material))