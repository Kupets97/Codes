from django.test import TestCase
from search_code.models import Code, Category


class CodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Test Category')
        Code.objects.create(code='00001', description='Test Code', category=category)

    def test_code_label(self):
        code = Code.objects.get(id=1)
        field_label = code._meta.get_field('code').verbose_name
        self.assertEqual(field_label, 'Код')

    def test_description_label(self):
        code = Code.objects.get(id=1)
        field_label = code._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Обозначение')

    def test_category_label(self):
        code = Code.objects.get(id=1)
        field_label = code._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'Категория')

    def test_clean_code(self):
        code = Code.objects.get(id=1)
        self.assertEqual(code.clean_code, '00001')

    def test_unique_clean_code(self):
        category = Category.objects.create(name='Test Category 2')
        Code.objects.create(code='00001', description='Test Code 2', category=category)
        code = Code.objects.get(id=2)
        self.assertEqual(code.clean_code, '00001_1')

    def setUp(self):
        self.category = Category.objects.create(name='TestCategory')

    def test_create_code(self):
        code = Code.objects.create(code='test', description='test code', category=self.category)
        self.assertEqual(code.code, 'test')
        self.assertEqual(code.description, 'test code')
        self.assertEqual(code.category, self.category)

    def test_save_clean_code(self):
        code = Code.objects.create(code=' test . code ', description='test code', category=self.category)
        self.assertEqual(code.clean_code, 'testcode')

    