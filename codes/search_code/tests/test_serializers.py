from django.test import TestCase
from search_code.models import Code, Category
from search_code.serializers import CodeSerialzier


class CodeSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Test Category')
        code = Code.objects.create(code='00001', description='Test Code', category=category)

    def test_code_serializer(self):
        code = Code.objects.get(id=1)
        serializer = CodeSerialzier(instance=code)
        expected_fields = {'code', 'description', 'category'}
        self.assertEqual(set(serializer.data.keys()), expected_fields)

    def test_category_serializer(self):
        code = Code.objects.get(id=1)
        serializer = CodeSerialzier(instance=code)
        expected_category = {'name': 'Test Category'}
        self.assertEqual(serializer.data['category'], expected_category)