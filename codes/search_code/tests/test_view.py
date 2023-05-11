from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from search_code.models import Category, Code, Relation
from search_code.serializers import CodeSerialzier
from search_code.views import CodeView


class CodeViewTestCase(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='TestCategory')
        self.parent_code = Code.objects.create(
            code='Code1', 
            description='Description1', 
            category=self.category
        )
        self.child_code1 = Code.objects.create(
            code=' Code 1.1', 
            description='Description 1.1', 
            category=self.category
        )
        self.child_code2 = Code.objects.create(
            code='Code 1.2 ', 
            description='Description 1.2', 
            category=self.category
        )
        Relation.objects.create(parent=self.parent_code, children=self.child_code1)
        Relation.objects.create(parent=self.parent_code, children=self.child_code2)
        self.valid_payload = {
            'code': 'Code1',
        }
        self.invalid_payload = {
            'code': 'InvalidCode',
        }
        
    def test_get_valid_code(self):
        response = self.client.get(
            reverse('code-list', kwargs={'code': 'Code1'}), 
            self.valid_payload, 
            format='json'
        )
        expected_data = CodeSerialzier([self.child_code1, self.child_code2], many=True).data
        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_invalid_code(self):
        response = self.client.get(
            reverse('code-list', kwargs={'code': 'InvalidCode'}), 
            self.invalid_payload, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
