from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from search_code.models import Code
from search_code.serializers import CodeSerializer

class CodeView(APIView):
    
    # выбираем все объекты модели Code
    queryset = Code.objects.all()
    # разрешаем доступ к API для всех пользователей
    permission_classes = (AllowAny,)

    # получаем queryset из базы данных, в котором категории будут присоединены к запросам
    def get_queryset(self):
        return self.queryset.select_related('category')

    # обработчик GET-запросов
    def get(self, request, code, *args, **kwargs):
        """
        Возвращает список сериализованных дочерних экземпляров модели Code, 
        принадлежащих родительскому экземпляру модели Code, чей код начинается с 
        переданной в параметре строки `code`. 

        Аргументы:
            code (str): строка для поиска.

        Возвращает:
            Список сериализованных дочерних экземпляров модели Code.
            
        Исключения:
            Http404: Если не найдены соответствующие экземпляры модели Code.
        """
        
        # убираем пробелы и точки в искомой строке
        clean_code = code.replace(' ', '').replace('.', '') 
        # ищем все дочерние экземпляры модели Code, у которых родительский экземпляр 
        # начинается с искомой строки `clean_code`
        child_codes = self.get_queryset().filter(children__parent__clean_code__startswith=clean_code)
        
        # если не найдены дочерние экземпляры модели Code, то генерируем исключение Http404
        if not child_codes:
            raise Http404("Не найдено вхождений строки кода '{}'".format(clean_code))

        # сериализуем список найденных экземпляров модели Code и возвращаем их в ответе
        serializer = CodeSerializer(instance=child_codes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

