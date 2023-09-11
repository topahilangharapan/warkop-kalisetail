from django.test import TestCase
from django.test import TestCase, Client

from main.models import Product
# Create your tests here.


class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def set_up_test_data(cls):
        Product.objects.create(name='Kopi Hitam w/Ampas', amount=5, description='Kopi Mantab', price=4000)

    def test_name_label(self):
        product = Product
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        product = Product()
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
