from dataclasses import dataclass
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from search_code.models import Code, Category, Relation
from codes.urls import urlpatterns


@dataclass
class CategoryNameData:
    okpd2 = '1'
    tnved = '2'

CODE_DATA_OKPD2 = {
    'code': '1010 10',
    'description': 'Мука',
    'category_id': 1,
}
CODE_DATA_TNVED = {
    'code': '300310',
    'description': 'Мука',
    'category_id': 2,
}

RELATION_DATA = {
    'parent_id': '1',
    'children_id': '2'
}




class CodeModelTest(TestCase):

    @classmethod
    def create_category(cls):
        Category.objects.create(name=CategoryNameData.okpd2)
        Category.objects.create(name=CategoryNameData.tnved)

    @classmethod
    def create_code(cls):
        Code.objects.create(**CODE_DATA_OKPD2)
        Code.objects.create(**CODE_DATA_TNVED)

    @classmethod
    def create_relation(cls):
        Relation.objects.create(**RELATION_DATA)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # instance = cls()
        cls.factory = APIClient()
        
        # Создаём тестовую запись в БД
        cls.create_category()
        cls.create_code()
        cls.create_relation()

    def test_code(self):
        URL = reverse('code', args=(CODE_DATA_OKPD2['code'],))
        response = self.factory.get(URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['code'], CODE_DATA_TNVED['code'])

    def test_category(self):
        name = Category.objects.get(id=1)
        self.assertEqual(name.name, CategoryNameData.okpd2)
        # self.assertEqual(name.name, CategoryNameData.tnved)

    def test_relation(self):
        parent = Relation.objects.get(parent_id=1)
        children = Relation.objects.get(children_id=2)
        self.assertEqual(parent.parent.code, CODE_DATA_OKPD2['code'])
        self.assertEqual(children.children.code, CODE_DATA_TNVED['code'])
        
        # Получаем из свойста класса Task значение verbose_name для title
        # verbose = task._meta.get_field('code').verbose_name
        # self.assertEqual(verbose, CategoryNameData.CODE)



    # def test_code_verbose_name(self):
    #     """verbose_name поля code совпадает с ожидаемым."""
    #     task = CodeModelTest.code
    #     # Получаем из свойста класса Task значение help_text для title
    #     verbose_name = task._meta.get_field('code').help_text
    #     self.assertEqual(verbose_name='Код')







# class SimpleTest(TestCase):
#     def setUp(self):
#         # Every test needs access to the request factory.
#         self.factory = RequestFactory()
#         self.user = Code.objects.create(
#             code='1001 01', description='Мука', category_id=4)
#         self.category = Category.objects.create(name=4)

#     def test_details(self):
#         # Create an instance of a GET request.
#         request = self.factory.get('code')

#         # Recall that middleware are not supported. You can simulate a
#         # logged-in user by setting request.user manually.
#         request.user = self.user
        

#         # Or you can simulate an anonymous user by setting request.user to
#         # an AnonymousUser instance.
#         request.user = AnonymousUser()
#         request.category = AnonymousUser()

#         # Test my_view() as if it were deployed at /customer/details
#         response = CodeView(request)
#         # Use this syntax for class-based views.
#         response = CodeView.as_view()(request)
#         self.assertEqual(response.status_code, 200)




    
    # @classmethod
    # def setUpTestData(cls):
    #     #Set up non-modified objects used by all test methods
    #     Code.objects.create(code='1001 10', description='код тнвед', category_id=3)

    # def test_code(self):
    #     author=Code.objects.get(id=1)
    #     field_label = author._meta.get_field('code').verbose_name
    #     self.assertEquals(field_label,'code')

    # def test_description(self):
    #     author=Code.objects.get(id=1)
    #     field_label = author._meta.get_field('test_description').verbose_name
    #     self.assertEquals(field_label,'код тнвед')

    # def test_first_name_max_length(self):
    #     code=Code.objects.get(id=1)
    #     max_length = code._meta.get_field('code').max_length
    #     self.assertEquals(max_length,10)

    # def test_object_code_and_description(self):
    #     code=Code.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (code.code, code.description)
    #     self.assertEquals(expected_object_name,str(code))

    # def test_get_absolute_url(self):
    #     code=Code.objects.get(id=1)
    #     #This will also fail if the urlconf is not defined.
    #     self.assertEquals(code.get_absolute_url(),'code/<str:code>')
    
    
    
    
    
    
    
    
    
    
    # def setUp(self):
    #     Code.objects.create(code="1001 10", description="Мука пшеничная", category_id=3)
    #     Code.objects.create(code="3001 13", description="Мука гречневая", category_id=4)

    # def test_answer(self):
    #     """Код и описание"""
    #     tnved = Code.objects.get(code="1001 10")
    #     okpd2 = Code.objects.get(code="3001 13")
    #     self.assertEqual(tnved, 'The 1001 10 "Мука пшеничная"')
    #     self.assertEqual(okpd2, 'The 3001 13 "Мука гречневая"')

    
    
    
    
    
    
    
    
    
    
    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     # Создаём тестовую запись в БД
    #     # и сохраняем созданную запись в качестве переменной класса
    #     cls.task = Code.objects.create(
    #         code='1001 10',
    #         description='Описание кода тнвед',
    #         category_id = 3
    #     )
    # def test_text_convert_to_slug(self):
    #     """Содержимое поля code преобразуется в code_test."""
    #     task = CodeModelTest.task
    #     code_test = task.code
    #     self.assertEqual(code_test, '1001 10')
    # def test_text_slug_max_length_not_exceed(self):
    #     """Длинный code обрезается и не превышает max_length поля code в модели."""
    #     task = CodeModelTest.task
    #     max_length_code = task._meta.get_field('code').max_length
    #     length_code = len(task.code)
    #     self.assertEqual(max_length_code, length_code) 
                
        
        
        
        
        # '''Проверка заполнения verbose_name'''
        # field_verboses = {'code': '1001 10',
        #                   'description': 'Описание кода',
        #                   }
        # for field, expected_value in field_verboses.items():
        #     with self.subTest(field=field):
        #         error_name = f'Поле {field} ожидало значение {expected_value}'
        #         self.assertEqual(
        #             self.post._meta.get_field(field).verbose_name,
        #             expected_value, error_name)
        
        
        
        
        
        
        # self.user = Code.objects.create_code(code='tnved')
        # self.group = Code.objects.create(code='1010 10',
        #                                   description='Описание кода',)
        # self.post = Post.objects.create(author=cls.code,
        #                                  text='Тестовое описание кода',)





        # url = reverse('code')
        # data = {'name': 'Code'}
        # reverse = self.client.get(url,data, format='json')
        # self.assertEqual(reverse.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Code.objects.all)
        # self.assertEqual(Code.objects.get(),name, 'Code')
        



